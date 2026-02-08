import matplotlib.pyplot as plt
import pandas as pd
import requests

# Getting data
station = "http://environment.data.gov.uk/flood-monitoring/id/stations/E1436/readings?_sorted"
response = requests.get(station) 
data = response.json()

# Processing data/putting it into a dataframe
df = pd.DataFrame(data["items"])
df["dateTime"] = pd.to_datetime(df["dateTime"])
df = df.sort_values("dateTime")

# User Inputs
startDate = input("Enter a start date (XXXX-XX-XX): ")  # User inputs starting date for Max River Level Line Graph...
endDate = input("Enter an end date (XXXX-XX-XX): ")  # User inputs end date for Max River Level Graph... (Note to Self: Ending it on a date makes it 00:00 on that day, so do the day after.)

filteredDf = df[(df["dateTime"] >= startDate) & (df["dateTime"] <= endDate)]  # Goes through the JSON data and filters the dates between the startDate and endDate variables.

# Line Graph Setup
plt.title("South Forty Foot Drain River Level at Boston Black Sluice") 
plt.xlabel("Date")
plt.ylabel("River Level (m)")
plt.grid(color = "green", linestyle = "--", linewidth = 0.5)  # Sets the grid up. Thin green dashed lines on both axis.
plt.axhline(y = 2.3, color = "red", linestyle ="-", label = "Flooding Possible above this level") # Shows on the graph what level (2.3m) and above flooding is possible at.
plt.legend()
plt.plot(filteredDf["dateTime"], filteredDf["value"], marker="o")  # Plots the points on the graph with a circle marker.

plt.show()  # Opens the graph in a seperate window.
