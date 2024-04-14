import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'Entity' column

merged_data = pd.read_csv("merged.csv")
merged_data['Entity'] = label_encoder.fit_transform(merged_data['Entity'])
columns_of_interest = ["Terrorist attacks", "Percentage of World Reserves", "Trade Freedom",
                       "Government Integrity", "Judicial Effectiveness","Entity"]

# Add constant term for regression
merged_data['const'] = 1
X = merged_data[columns_of_interest]

# Define dependent variables (Lockheed Martin and General Dynamics)
y_lockheed = merged_data['Lockheed Martin (Billion USD)']
y_general_dynamics = merged_data['General Dynamics (Billion USD)']

# Perform multiple linear regression for Lockheed Martin
model_lockheed = sm.OLS(y_lockheed, X).fit()

# Perform multiple linear regression for General Dynamics
model_general_dynamics = sm.OLS(y_general_dynamics, X).fit()

# Print regression results for Lockheed Martin
print("Regression Results for Lockheed Martin (Billion USD):")
print(model_lockheed.summary())

# Print regression results for General Dynamics
print("\nRegression Results for General Dynamics (Billion USD):")
print(model_general_dynamics.summary())