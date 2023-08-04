import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import numpy as np

# Read the CSV file into a DataFrame, skipping the header row
data = pd.read_csv('2023-uwa.csv', skiprows=1)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Convert 'Temperature' column to numeric values, ignoring non-numeric entries
data['Temperature'] = pd.to_numeric(data['Temperature'], errors='coerce')

# Convert Fahrenheit to Celsius
data['Temperature'] = (data['Temperature'] - 32) * 5/9

# Set up the plot
fig, ax1 = plt.subplots(1, figsize=(8, 10))

# Format the x-axis to display month and day
months = mdates.MonthLocator()
days = mdates.DayLocator()
month_day_fmt = mdates.DateFormatter('%m/%d')
ax1.xaxis.set_major_locator(months)
ax1.xaxis.set_minor_locator(days)
ax1.xaxis.set_major_formatter(month_day_fmt)

# Replace ignored values with NaN
data['Temperature'] = data['Temperature'].where(data['Temperature'].notna(), np.nan)

# Plot the scatter plot with fixed color, adjusted opacity, and no marker edge color
sc = ax1.scatter(data['Date'], data['Temperature'], c='blue', alpha=0.1, edgecolors='none')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('2023 UWA Temperature')

# Calculate statistics per date
daily_stats = data.groupby(data['Date'].dt.date)['Temperature'].agg(['mean', 'median', lambda x: np.percentile(x, 25), lambda x: np.percentile(x, 75)])
daily_stats.columns = ['Mean', 'Median', '25th Percentile', '75th Percentile']

# Add legend
ax1.legend()

# Adjust the y-axis ticks
ax1.yaxis.set_major_locator(MultipleLocator(1))

# Adjust the layout and spacing
plt.tight_layout()

# Display the plot
plt.show()
