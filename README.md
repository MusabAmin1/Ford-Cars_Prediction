🚗 Ford Car Price Prediction Project

1 - Overview:
This project predicts the price of used Ford cars using Machine Learning regression models. The workflow includes data cleaning, exploratory data analysis (EDA), feature engineering, and model training.

Multiple regression algorithms including Linear Regression, KNN Regressor, Decision Tree Regressor, and Random Forest Regressor are evaluated. Random Forest is further tuned using RandomizedSearchCV for improved performance.

A Streamlit web application is used for real-time price prediction based on user inputs.

2 - Files:
ford_app.py
ford_model.pkl
ford.csv
ford.ipynb

3 - Installation:
Install Python (recommended ≥ 3.10)

Install required libraries:
pip install numpy pandas matplotlib seaborn scikit-learn scipy streamlit joblib

4 - Usage:
Clone the repository:
git clone <repository_url>
cd <project_folder>

Run the Streamlit app:
streamlit run ford_app.py

Enter car details such as model, year, mileage, fuel type, transmission, tax, mpg, and engine size to get predicted price.

5 - Data Processing & EDA:
Removed duplicate records
Handled missing and incorrect values
Filtered unrealistic year values (year < 2026)
Replaced invalid engineSize values (0 → mode)
Performed univariate and bivariate analysis using histograms and scatter plots
Correlation analysis using heatmap

Categorical variables were encoded using One-Hot Encoding (drop_first=True).

Chi-square test was applied for feature selection, and only statistically significant features were retained.

6 - Models Used:
The following regression models were trained and evaluated:

Linear Regression
K-Nearest Neighbors Regressor
Decision Tree Regressor
Random Forest Regressor

7 - Model Evaluation:
Models were evaluated using:

R² Score
Adjusted R² Score

Random Forest Regressor performed the best among all base models.

8 - Hyperparameter Tuning:
Random Forest was optimized using RandomizedSearchCV with:

n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features

Final model achieved improved and stable performance compared to base models.

9 - Final Model:
Algorithm: Random Forest Regressor (Tuned)
Compression: joblib (compress=3)
Saved Model: ford_model.pkl

10 - Notes:
Scaling was applied only for Linear Regression and KNN
Decision Tree and Random Forest were trained on raw features
No ensemble stacking or boosting techniques were used
Model was selected based on best R² and stability
Streamlit app ensures real-time prediction interface

🔥 Final Summary:
This project demonstrates a complete machine learning pipeline including:

Data cleaning
Feature engineering
Model comparison
Hyperparameter tuning
Deployment using Streamlit
