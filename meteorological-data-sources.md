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
Although this code successfully pulled weather data points for temperature, precipitation, humidity, lunar phase, and wind speed, the documentation on NWS was somewhat cryptic. 
Writing scripts to access the amount of data points that I needed, and then somehow verifying seemed like a monumental task not suitable for me coding skills and the amount of time I have to complete this project (<8 weeks). 

## Oikolab

[Oikolab](oikolab.com) offers a simple way to download historical meterological data in the form of a .csv file. Their *About Me* page states that
they pull "raw data from primary sources such as ECWMF and NOAA."
According to their documentation page, they use ERA5 (climate reanalysis software produced by [ECMWF](https://climate.copernicus.eu/climate-reanalysis))
to "combine vast observations from satellites, aircraft, land and sea based weather sensors with atmospheric models to generate consistent time series of multiple climate variables."

This appears to be a great resource. However, verification was desired, which requires data from a known reliable source. 

## Meteostat 

Meteostat is a python package available on github. It appears to be a powerful tool to pull weather data from various stations. 
After working with their documentation to pull data, it looked promising. However, upon further investigation of the station said data was pulled from, 
the closest available was at South Park, an area of South Seattle near the Museum of Flight. Because this was not close enough to UBNA, this data was deemed unusable. 

## UW's Department of Atmospheric Science's Weather Stations

After meeting with David Warren, the search was finally concluded. 

The data we needed was available through their [time series plots tool](http://www-k12.atmos.washington.edu/k12/grayskies/nw_weather.html).

This script will pull data from UWA station hourly and update the .csv file: 

```python
import csv
import requests
import datetime
import schedule
import time

# Define the URL and parameters for fetching the data
url = "http://www-k12.atmos.washington.edu/k12/grayskies/plot_nw_wx.cgi"
params = {
    "Measurement": ["Temperature", "Relhum", "Speed", "Direction", "Pressure", "Solar", "SumRain", "Rain"],
    "station": "UWA",
    "interval": "0",
    "timezone": "0",
    "rightlab": "y",
    "connect": "dataonly",
    "groupby": "overlay",
    "begmonth": "6",
    "begday": "1",
    "begyear": "2023",
    "beghour": "0",
    "endmonth": str(datetime.datetime.now().month),
    "endday": str(datetime.datetime.now().day),
    "endyear": str(datetime.datetime.now().year),
    "endhour": "23"
}

csv_file = "2023-uwa.csv"

def fetch_data():
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.text

        # Write the data to a CSV file
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            for row in data.splitlines():
                split_data = row.split(",")
                writer.writerow(split_data)

        print(f"Data fetched and saved successfully. File saved at: {csv_file}")

def job():
    print("Checking for new data...")
    fetch_data()
    print("Data fetch and save completed.")

# Run the job immediately when you press "run"
job()

# Schedule the job to run every hour
schedule.every().hour.do(job)

# Run the scheduler in an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)
```

