import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv("merged.csv")

from sklearn.preprocessing import LabelEncoder

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'Entity' column
data['Entity'] = label_encoder.fit_transform(data['Entity'])

# Split the data into features (X) and target variable (y)
X = data.drop(['Lockheed Martin (Billion USD)', 'General Dynamics (Billion USD)','Country','Year','Unnamed: 0_y','Unnamed: 0_x'], axis=1)
y = data['Lockheed Martin (Billion USD)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_regressor.fit(X_train, y_train)

# Make predictions on the training set
y_train_pred = rf_regressor.predict(X_train)

# Make predictions on the test set
y_test_pred = rf_regressor.predict(X_test)

# Calculate Mean Squared Error on training set
mse_train = mean_squared_error(y_train, y_train_pred)
print("Mean Squared Error (Training):", mse_train)

# Calculate Mean Squared Error on test set
mse_test = mean_squared_error(y_test, y_test_pred)
print("Mean Squared Error (Test):", mse_test)

# Feature importance analysis
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': rf_regressor.feature_importances_})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.bar(feature_importance['Feature'], feature_importance['Importance'])
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.xticks(rotation=25)
plt.show()