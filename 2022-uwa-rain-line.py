import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import numpy as np

# Read the CSV file into a DataFrame, skipping the header row
data = pd.read_csv('2022-uwa-cleaned.csv', skiprows=1)

# Set up the plot
fig, ax1 = plt.subplots(1, figsize=(8, 10))

# Format the x-axis to display Pseudo-Julian-Date
ax1.xaxis.set_major_locator(MultipleLocator(30))  # Set major tick every 30 days
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Display Pseudo-Julian-Date as YYYY-MM format

# Create temperature gradient colormap
cmap = plt.cm.get_cmap('Blues_r')

# Calculate statistics per date
daily_stats = data.groupby(' Pseudo-Julian-Date')['Rain'].agg(['mean', 'median', lambda x: np.percentile(x, 25), lambda x: np.percentile(x, 75)])
daily_stats.columns = ['Mean', 'Median', '25th Percentile', '75th Percentile']

# Plot the bar graph with temperature gradient colors
bar = ax1.bar(data[' Pseudo-Julian-Date'], data['Rain'], color=cmap(data['Rain']), alpha=0.7)
ax1.set_ylabel('Rain')
ax1.set_title('Rain Bar Graph')

# Adjust the y-axis ticks
ax1.yaxis.set_major_locator(MultipleLocator(1))

# Add colorbar
norm = plt.Normalize(data['Rain'].min(), data['Rain'].max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # Dummy array for the colorbar
cbar = fig.colorbar(sm, ax=ax1)
cbar.set_label('Rain')

# Adjust the layout and spacing
plt.tight_layout()

# Display the plot
plt.show()

