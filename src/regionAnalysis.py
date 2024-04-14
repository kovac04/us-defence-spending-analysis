import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("merged_with_region.csv")

# Group the data by region and count the number of terrorist attacks in each region
terrorist_attacks_by_region = df.groupby('region')['Terrorist attacks'].sum()

#Plotting
plt.figure(figsize=(8, 8))
plt.pie(terrorist_attacks_by_region, labels=terrorist_attacks_by_region.index, autopct='%1.1f%%', startangle=140)
plt.title('Number of Terrorist Attacks by Region')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


