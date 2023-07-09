# Collection of Meteorological Observational Data

There are many places and ways to collect meterogolocial data. For this project, a few considerations were 
important for choosing the best source. 
* In order for analysis alongside bat calls recorded via the Union Bay Bats project by Dr. Wu-Jung at the University of Washington's Applied Physics Lab, ** hourly weather data from a station as nearby UBNA ** was needed.
* That local data also needed to coincide with the bat call recording season (June 2022-Oct 2022, June 2023-Present)
* The data needed to be from a reliable weather source

## NOAA

Though NOAA collects weather data across the entire country (which is accessible through many avenues on their website, such as the Climate Data Online tool), 
the closest stations (station x,y,z) all either only collected precipitation data or did not collect data for the desired time frame. 

## The National Weather Service

A subset of NOAA, The National Weather Service (NWS) likely holds weather records much like what this project sought. 
To access NWS's weather data, an API is needed. The following code was created using my own limited coding abilities alongside ChatGPT. 
```python
import csv
import xlsxwriter

# Assuming the JSON response is stored in a variable called 'response'
response = {
    # JSON response data...
}

# Extract the desired data from the response
location = 'Union Bay Natural Area'
state = response['properties']['relativeLocation']['properties']['state']
start_time = '2023-06-26T10:00:00-07:00'
end_time = '2023-06-26T11:00:00-07:00'
temperature = 75
precipitation = 0
wind_speed = '10 mph'
humidity = 70

# Open the CSV file in write mode
csv_file_path = 'weather_data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['Location', 'State', 'Start Time', 'End Time', 'Temperature', 'Precipitation', 'Wind Speed', 'Humidity'])
    
    # Write the data row
    writer.writerow([location, state, start_time, end_time, temperature, precipitation, wind_speed, humidity])

# Create the XLSX file with bold headers and fitted cells
xlsx_file_path = 'weather_data.xlsx'
workbook = xlsxwriter.Workbook(xlsx_file_path)
worksheet = workbook.add_worksheet()

# Add a format for the bold headers
bold_format = workbook.add_format({'bold': True})

# Write the headers with the bold format
headers = ['Location', 'State', 'Start Time', 'End Time', 'Temperature', 'Precipitation', 'Wind Speed', 'Humidity']
for col, header in enumerate(headers):
    worksheet.write(0, col, header, bold_format)
    # Automatically adjust the column width based on the content
    worksheet.set_column(col, col, len(header))

# Write the data row
data = [location, state, start_time, end_time, temperature, precipitation, wind_speed, humidity]
for col, value in enumerate(data):
    worksheet.write(1, col, value)

# Close the workbook
workbook.close()

print(f'CSV and XLSX files saved at: {csv_file_path}, {xlsx_file_path}')
```
Although this code successfully pulled weather data points for temperature, humidity, wind speed,  