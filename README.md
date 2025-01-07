
# Top Asian Universities - QS Rankings 2024 Dashboard

## Overview

This project is an interactive data analytics dashboard built to visualize and analyze data from the QS World University Rankings 2024, focusing on Asian universities. The dashboard allows users to explore trends, correlations, and predictions about university rankings using statistical techniques and machine learning models. It is designed with an intuitive user interface and multiple interactive features to enhance the data exploration experience.

## Features

### 1. Home Tab
- Display the uploaded dataset in a tabular format for quick data review.

### 2. Regional Analysis
- Visualize the number of universities by country.
- Interactive filters to explore data for specific countries.
- Dynamic bar charts created using Plotly for better insights.

### 3. Correlation Heatmap
- Explore correlations between various numerical features.
- Heatmap visualization using Seaborn for statistical analysis.

### 4. Scatter Plots
- Create scatter plots between any two numerical variables.
- Visualize relationships and patterns in the dataset.

### 5. Clustering Universities
- Perform K-means clustering on selected features.
- 3D scatter plots using Plotly to visualize clusters of universities.

### 6. Rank Prediction
- Use Linear Regression to predict university rankings based on selected features.
- Compare predicted rankings with actual rankings via interactive scatter plots.

### 7. Data Input
- Upload your CSV files directly into the dashboard.
- Automated preprocessing to handle missing or non-numeric data.

## Technical Stack

### 1. Programming Language
- Python 3.8+

### 2. Libraries and Frameworks
- **Streamlit**: For building the interactive dashboard.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Plotly**: For creating interactive plots and visualizations.
- **Seaborn & Matplotlib**: For advanced statistical and data visualization.
- **scikit-learn**: For machine learning (clustering and regression).

### 3. Hosting and Deployment
- Hosted on Streamlit Cloud (or deployable on Heroku/AWS).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/top-asian-universities.git
   cd top-asian-universities
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Upload a dataset (CSV file) to start exploring the data.

## Data Preprocessing
- Handles missing and non-numeric data automatically.
- Features for clustering and regression can be selected interactively.

## How It Works

1. Upload a CSV file containing university data (e.g., rank, scores, and attributes).
2. Navigate through tabs for different analyses:
   - **Regional Analysis**: Understand country-wise university distribution.
   - **Correlation Heatmap**: Visualize feature correlations.
   - **Scatter Plots**: Identify trends between selected variables.
   - **Clustering Universities**: Group universities based on similarities.
   - **Rank Prediction**: Predict university ranks using linear regression.
3. Download processed data and insights as needed.

## Applications

- Academic and industry researchers exploring university performance.
- Students and parents evaluating universities for higher education.
- Policymakers and education consultants studying regional trends.


## Credits

Developed by **Fawad Mughal**, leveraging Python's powerful data science ecosystem and interactive tools like Streamlit and Plotly.

## Connect With Me

- **[LinkedIn](https://www.linkedin.com/in/fawad-mughal/)**  
- **[GitHub](https://github.com/fawadmughal-ds/)**  
- Email: help.fawadmughal@gmail.com

## License

This project is licensed under the MIT License. See the LICENSE file for details.
