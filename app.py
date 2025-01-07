import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import plotly.express as px


st.set_page_config(page_title="Top Asian Universities", page_icon="🏫", layout="wide")

st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #1f77b4;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            font-weight: bold;
            color: white;
            box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        }
        .header {
            background: linear-gradient(90deg, #1f77b4, #4a90e2);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: -40px -20px 20px -20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        .header h1 {
            font-size: 2.5rem;
            margin: 0;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .header-icon {
            font-size: 2.8rem;
            margin-right: 10px;
            vertical-align: middle;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
            overflow-x: auto;
        }
        
        .stTabs [data-baseweb="tab"] {
            position: relative;
            padding: 10px 20px;
            background-color: #f0f2f6;
            border-radius: 4px 4px 0 0;
            gap: 2px;
            margin-right: 2px;
            color: #31333F;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #e0e2e6;
        }
        
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            background-color: #ffffff;
            color: #31333F;
        }

        .stTabs [data-baseweb="tab-list"] button[aria-selected="false"] {
            background-color: #f0f2f6;
            color: #31333F;
        }

        /* Close button styling */
        .close-btn {
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            border: none;
            background: transparent;
            color: #666;
            cursor: pointer;
            padding: 0 5px;
            font-size: 14px;
            line-height: 1;
            transition: color 0.2s;
        }

        .close-btn:hover {
            color: #ff4444;
        }

        /* Sidebar styling */
        .css-1d391kg {  /* Sidebar */
            background-color: #f8f9fa;
            padding: 2rem 1rem;
            border-right: 1px solid #e9ecef;
        }

        /* Sidebar title */
        .css-1d391kg h1 {
            color: #1f77b4;
            font-size: 1.5rem;
            margin-bottom: 2rem;
            text-align: center;
            font-weight: 600;
        }

        /* Sidebar buttons */
        .stButton > button {
            width: 100%;
            border: none;
            padding: 0.75rem 1rem;
            margin: 0.5rem 0;
            border-radius: 8px;
            background-color: #ffffff;
            color: #31333F;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .stButton > button:hover {
            background-color: #1f77b4;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        /* Divider */
        hr {
            margin: 2rem 0;
            border: none;
            border-top: 1px solid #e9ecef;
        }

        /* File uploader */
        .css-1x8cf1d {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        /* Small close button styling */
        .small-close-btn {
            font-size: 12px;
            padding: 0px 6px;
            border-radius: 4px;
            border: none;
            background: transparent;
            color: #666;
            cursor: pointer;
            transition: color 0.2s;
        }

        .small-close-btn:hover {
            color: #ff4444;
        }

        /* Adjust column spacing for close button */
        [data-testid="column"] {
            padding: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

if 'active_tabs' not in st.session_state:
    st.session_state.active_tabs = {"Home"}  
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Home"  
if 'tab_id' not in st.session_state:
    st.session_state.tab_id = 0
if 'tab_states' not in st.session_state:
    st.session_state.tab_states = {}
if 'last_active_tab' not in st.session_state:
    st.session_state.last_active_tab = None
if 'active_tab_index' not in st.session_state:
    st.session_state.active_tab_index = 0

def handle_tab_change(tab_name):
    st.session_state.current_tab = tab_name
    st.session_state.last_active_tab = tab_name
    if tab_name not in st.session_state.tab_states:
        st.session_state.tab_states[tab_name] = True
    st.session_state.tab_id += 1

def footer():
    st.markdown("""
        <div class="footer">
            Developed by Fawad Mughal.
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="header">
        <h1><span class="header-icon">🏫</span> Top Asian Universities - QS Rankings 2024</h1>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<h1>📊 Analysis Tools</h1>", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.markdown("### 🏠 Main")
if st.sidebar.button("Home", key="home_btn"):
    st.session_state.active_tabs.add("Home")
    st.session_state.current_tab = "Home"

st.sidebar.markdown("### 📈 Basic Analysis")
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("Regional", key="regional_btn"):
        st.session_state.active_tabs.add("Regional Analysis")
        st.session_state.current_tab = "Regional Analysis"

with col2:
    if st.button("Correlation", key="correlation_btn"):
        st.session_state.active_tabs.add("Correlation Heatmap")
        st.session_state.current_tab = "Correlation Heatmap"

st.sidebar.markdown("### 🔍 Advanced Analysis")
col3, col4 = st.sidebar.columns(2)
with col3:
    if st.button("Scatter", key="scatter_btn"):
        st.session_state.active_tabs.add("Scatter Plots")
        st.session_state.current_tab = "Scatter Plots"

with col4:
    if st.button("Clustering", key="clustering_btn"):
        st.session_state.active_tabs.add("Clustering Universities")
        st.session_state.current_tab = "Clustering Universities"

if st.sidebar.button("Rank Prediction", key="prediction_btn"):
    st.session_state.active_tabs.add("Rank Prediction")
    st.session_state.current_tab = "Rank Prediction"

st.sidebar.markdown("---")
st.sidebar.markdown("### 📁 Data Input")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    def preprocess_data(data):
        numeric_cols = data.select_dtypes(include=[float, int]).columns
        for col in numeric_cols:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        return data

    data = preprocess_data(data)

    if st.session_state.active_tabs:
        tab_list = list(st.session_state.active_tabs)
        tabs = st.tabs(tab_list)
        
        for tab, tab_name in zip(tabs, tab_list):
            with tab:
                col1, col2 = st.columns([0.97, 0.03])  # Adjust ratio to make close button column smaller
                with col2:
                    if st.button("×", key=f"close_{tab_name}", help="Close tab"):
                        st.session_state.active_tabs.remove(tab_name)
                        if len(st.session_state.active_tabs) > 0:
                            st.session_state.current_tab = list(st.session_state.active_tabs)[0]
                        else:
                            st.session_state.active_tabs.add("Home")
                            st.session_state.current_tab = "Home"
                        st.rerun()
                
                if tab_name == "Home":
                    st.subheader("Welcome to the Top Asian Universities Dashboard")
                    st.dataframe(data.head())
                elif tab_name == "Regional Analysis":
                    st.subheader("Regional Analysis")
                    st.write("### Number of Universities by Country")
                    country_counts = data["Country"].value_counts().sort_values()

                    country = st.selectbox("Filter by Country (Optional)", ["All"] + list(data["Country"].unique()))
                    if country != "All":
                        filtered_data = data[data["Country"] == country]
                    else:
                        filtered_data = data

                    fig = px.bar(
                        filtered_data["Country"].value_counts(),
                        x=filtered_data["Country"].value_counts().index,
                        y=filtered_data["Country"].value_counts().values,
                        labels={"x": "Country", "y": "Number of Universities"},
                        title="Number of Universities by Country",
                    )
                    fig.update_layout(autosize=True, xaxis_title="Country", yaxis_title="Count")
                    st.plotly_chart(fig, use_container_width=True)

                elif tab_name == "Correlation Heatmap":
                    st.subheader("Correlation Heatmap")
                    numeric_data = data.select_dtypes(include=[float, int])
                    fig, ax = plt.subplots(figsize=(12, 10))
                    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", cbar_kws={"shrink": 0.8}, ax=ax)
                    st.pyplot(fig)

                elif tab_name == "Scatter Plots":
                    st.subheader("Scatter Plots")
                    x_axis = st.selectbox("Choose X-axis", data.select_dtypes(include=[float, int]).columns)
                    y_axis = st.selectbox("Choose Y-axis", data.select_dtypes(include=[float, int]).columns)
                    fig = px.scatter(
                        data,
                        x=x_axis,
                        y=y_axis,
                        title=f"{y_axis} vs {x_axis}",
                        labels={"x": x_axis, "y": y_axis},
                        color_discrete_sequence=["#1f77b4"],
                    )
                    fig.update_layout(autosize=True)
                    st.plotly_chart(fig, use_container_width=True)

                elif tab_name == "Clustering Universities":
                    st.subheader("Clustering Universities")
                    cluster_features = st.multiselect(
                        "Select features for clustering", data.select_dtypes(include=[float, int]).columns
                    )
                    if len(cluster_features) > 1:
                        scaler = StandardScaler()
                        X_scaled = scaler.fit_transform(data[cluster_features].dropna())

                        kmeans = KMeans(n_clusters=3, random_state=42).fit(X_scaled)
                        data["Cluster"] = kmeans.labels_

                        fig = px.scatter_3d(
                            data,
                            x=cluster_features[0],
                            y=cluster_features[1],
                            z=cluster_features[2] if len(cluster_features) > 2 else cluster_features[1],
                            color="Cluster",
                            title="University Clusters",
                            color_continuous_scale="Viridis",
                        )
                        st.plotly_chart(fig)

                elif tab_name == "Rank Prediction":
                    st.subheader("Rank Prediction")
                    features = st.multiselect(
                        "Select features for regression", data.select_dtypes(include=[float, int]).columns
                    )
                    if "Rank" in data.columns and len(features) > 0:
                        X = data[features].dropna()
                        y = data.loc[X.index, "Rank"]

                        model = LinearRegression().fit(X, y)
                        data["Predicted Rank"] = model.predict(X)

                        fig = px.scatter(
                            data,
                            x="Predicted Rank",
                            y="Rank",
                            title="Predicted vs Actual Rank",
                            labels={"x": "Predicted Rank", "y": "Actual Rank"},
                            color_discrete_sequence=["#1f77b4"],
                        )
                        st.plotly_chart(fig)

    footer()
