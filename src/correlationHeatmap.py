import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load data
data = pd.read_csv('merged_with_region.csv')

freedom_vars = ['Government Integrity', 'Judicial Effectiveness', 'Trade Freedom', 'Property Rights']
region_var = 'region'

# Step 3: One-hot encode the 'region' variable
data_encoded = pd.get_dummies(data, columns=[region_var])

# Step 4: Subset data
subset_data = data_encoded[freedom_vars + [col for col in data_encoded.columns if region_var in col]]


# Create a new variable that is a combination of the existing variables
subset_data['Combined'] = subset_data[freedom_vars].mean(axis=1)

# Apply the transformation
subset_data = subset_data.applymap(lambda x: (x - 1.5)**2 if x < 0 else (x + 1.5)**2)

# Step 6: Calculate correlation
correlation_matrix = subset_data.corr()

# Create a list of the region columns
region_cols = [col for col in data_encoded.columns if region_var in col]

# Create a new DataFrame that only includes the correlations between the freedom variables and the region variables
correlation_matrix_regions_vs_freedom = correlation_matrix.loc[freedom_vars, region_cols]

# Step 7: Visualize correlation
plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix_regions_vs_freedom, annot=True, cmap='coolwarm', fmt=".2f")

plt.title('Correlation Heatmap between Freedom Variables and Region')
plt.xticks(rotation=15)
plt.show()