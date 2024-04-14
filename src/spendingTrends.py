import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('US-defence.csv')


plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Lockheed Martin (Billion USD)'], label='Lockheed Martin')
plt.plot(data['Year'], data['General Dynamics (Billion USD)'], label='General Dynamics')
plt.xlabel('Year')
plt.ylabel('Spending (Billion USD)')
plt.title('Spending Trend of Lockheed Martin and General Dynamics')
plt.legend()
plt.grid(True)
plt.show()