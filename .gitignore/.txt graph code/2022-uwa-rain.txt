import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import numpy as np

# Read the CSV file into a DataFrame, skipping the header row
data = pd.read_csv('2022-uwa-cleaned.csv', skiprows=1)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set up the plot
fig, ax1 = plt.subplots(1, figsize=(8, 10))

# Format the x-axis to display month and day
months = mdates.MonthLocator()
days = mdates.DayLocator()
month_day_fmt = mdates.DateFormatter('%m/%d')
ax1.xaxis.set_major_locator(months)
ax1.xaxis.set_minor_locator(days)
ax1.xaxis.set_major_formatter(month_day_fmt)

# Set the x-axis limits
start_date = pd.to_datetime('2022-06-01')
end_date = pd.to_datetime('2022-11-01')
ax1.set_xlim(start_date, end_date)

# Plot the scatter plot with baby blue color and adjusted opacity
sc = ax1.scatter(data['Date'], data['Rain'], c='skyblue', alpha=1)
ax1.set_ylabel('Rain')
ax1.set_title('2022 UWA Rainfall')

# Calculate statistics per date
daily_stats = data.groupby('Date')['Rain'].agg(['mean', 'median', lambda x: np.percentile(x, 25), lambda x: np.percentile(x, 75)])
daily_stats.columns = ['Mean', 'Median', '25th Percentile', '75th Percentile']

# Add trendlines
ax1.plot(daily_stats.index, daily_stats['Mean'], color='navy', linestyle='--', label='Mean')

# Add legend
ax1.legend()

# Adjust the y-axis ticks
ax1.yaxis.set_major_locator(MultipleLocator(0.005))

# Adjust the layout and spacing
plt.tight_layout()

# Display the plot
plt.show()

