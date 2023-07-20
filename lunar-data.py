import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Read the data from the Excel file with the correct date format
data = pd.read_excel('LUNAR.xlsx', parse_dates=['Date'], date_format='%Y %b %d')

# Function to convert moon phases to numerical values
def moon_phase_to_numeric(phase):
    if phase == 1:
        return 0
    elif phase == 0.75:
        return 1
    elif phase == 0.25:
        return -1
    elif phase == 0:
        return 0

# Convert moon phases to numerical values
data['Moon Phase Numeric'] = data['Moon Phase'].apply(moon_phase_to_numeric)

# Filter data for the specified date ranges
start_date_2022 = pd.to_datetime('2022-05-01')
end_date_2022 = pd.to_datetime('2022-11-01')
start_date_2023 = pd.to_datetime('2023-05-29')
end_date_2023 = pd.to_datetime('2023-11-01')

data_2022 = data[(data['Date'] >= start_date_2022) & (data['Date'] <= end_date_2022)]
data_2023 = data[(data['Date'] >= start_date_2023) & (data['Date'] <= end_date_2023)]

# Generate the x values for sine waves (the date part from the 'Date' column)
x_2022 = data_2022['Date']
x_2023 = data_2023['Date']

# Generate the y values for sine waves (numerical values of moon phases)
y_2022 = data_2022['Moon Phase Numeric']
y_2023 = data_2023['Moon Phase Numeric']

# Create the sine wave for 2022 and 2023
t_2022 = np.linspace(0, 2 * np.pi, len(x_2022))
sine_wave_2022 = np.sin(t_2022)

t_2023 = np.linspace(0, 2 * np.pi, len(x_2023))
sine_wave_2023 = np.sin(t_2023)

# Plot the sine waves of moon phases for 2022 and 2023
plt.figure(figsize=(10, 10))

# Plot 2022
plt.subplot(2, 1, 1)
plt.plot(x_2022, sine_wave_2022, color='b', label='Moon Phase')
plt.scatter(mdates.date2num(x_2022[y_2022 == 1]), sine_wave_2022[y_2022 == 1], color='g', marker='o', label='Last Quarter')
plt.scatter(mdates.date2num(x_2022), y_2022, color='r', marker='o', label='Data Points')
plt.title('Moon Phases 2022')
plt.xlabel('Date')
plt.ylabel('Moon Phase')
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1], ['First Quarter', 'New Moon', 'Full Moon'])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

# Plot 2023
plt.subplot(2, 1, 2)
plt.plot(x_2023, sine_wave_2023, color='b', label='Moon Phase')
plt.scatter(mdates.date2num(x_2023[y_2023 == 1]), sine_wave_2023[y_2023 == 1], color='g', marker='o', label='Last Quarter')
plt.scatter(mdates.date2num(x_2023), y_2023, color='r', marker='o', label='Data Points')
plt.title('Moon Phases 2023')
plt.xlabel('Date')
plt.ylabel('Moon Phase')
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1], ['First Quarter', 'New Moon', 'Full Moon'])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.tight_layout()

# Show the plots
plt.show()












