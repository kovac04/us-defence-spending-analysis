

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the data
data = pd.read_csv("merged.csv")
# Filter out rows with terrorist attacks
terrorist_attacks = data[data['Terrorist attacks'] > 0]

# Group by country and calculate the change in spending
change_in_spending = terrorist_attacks.groupby('Entity')[['Lockheed Martin (Billion USD)', 'General Dynamics (Billion USD)']].sum()

# Calculate the percentage change in spending
change_in_spending['Lockheed Martin Change (%)'] = (change_in_spending['Lockheed Martin (Billion USD)'] / change_in_spending['Lockheed Martin (Billion USD)'].sum()) * 100
change_in_spending['General Dynamics Change (%)'] = (change_in_spending['General Dynamics (Billion USD)'] / change_in_spending['General Dynamics (Billion USD)'].sum()) * 100

# Sort the data by the change in Lockheed Martin spending
change_in_spending_sorted = change_in_spending.sort_values(by='Lockheed Martin Change (%)', ascending=False)

# Plot the data
plt.figure(figsize=(12, 8))
change_in_spending_sorted[['Lockheed Martin Change (%)', 'General Dynamics Change (%)']].plot(kind='bar', stacked=True)
plt.title('Change in Spending After Terrorist Attacks by Country')
plt.xlabel('Country')
plt.ylabel('Percentage Change in Spending')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()