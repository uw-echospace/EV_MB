import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import numpy as np

# Read the CSV file into a DataFrame, skipping the header row
data = pd.read_csv('2022-uwa.csv', skiprows=1)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set up the plot
fig, ax1 = plt.subplots(1, figsize=(8, 10))

# Calculate statistics per date
daily_stats = data.groupby(data['Date'].dt.date)[['Relhum', 'Speed', 'Gust']].agg(
    {'Relhum': ['mean', 'median', lambda x: np.percentile(x, 25), lambda x: np.percentile(x, 75)],
     'Speed': 'mean',
     'Gust': 'max'}
)
daily_stats.columns = ['Relhum Mean', 'Relhum Median', 'Relhum 25th Percentile', 'Relhum 75th Percentile',
                       'Speed Mean', 'Max Gust']

# Format the x-axis to display month and day
month_day_fmt = mdates.DateFormatter('%m/%d')
ax1.xaxis.set_major_formatter(month_day_fmt)

# Plot the scatter plot with solid blue color
sc = ax1.scatter(data['Date'], data['Speed'], c='skyblue', alpha=1)  # Set c to 'skyblue'

ax1.set_ylabel('Speed')
ax1.set_title('2023 UWA Speed and Max Gust')

# Plot trendlines per date
ax1.plot(daily_stats.index, daily_stats['Speed Mean'], color='black', linestyle='--', label='Speed Mean')

# Add legend
ax1.legend()

# Adjust the y-axis ticks
ax1.yaxis.set_major_locator(MultipleLocator(1))

# Add second y-axis for Max Gust
ax2 = ax1.twinx()
ax2.plot(daily_stats.index, daily_stats['Max Gust'], color='blue', linestyle='-', label='Max Gust')
ax2.set_ylabel('Max Gust')

# Add legend for the second y-axis
ax2.legend(loc='lower right')

# Adjust the layout and spacing
plt.tight_layout()

# Display the plot
plt.show()
