import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("CSV/black-sluice-ps-boston-lincolnshire-070226.csv")  # Read Comma Separated Value (CSV) file for station data.
df["date"] = pd.to_datetime(df["date"])  # Date column (currently text strings in csv file) --> datetime 

startDate = input("Enter a start date (XXXX-XX-XX): ")  # User inputs starting date for Max River Level Line Graph...
endDate = input("Enter an end date (XXXX-XX-XX): ")  # User inputs end date for Max River Level Graph...

filteredDf = df[(df["date"] >= startDate) & (df["date"] <= endDate)] # Goes through every... single... row... in the csv file and filters the dates between the startDate and endDate variables (In this case 2025-01-01 to 2025-01-15, to see the  maximum river levels around when the South Forty Foot flooded.)

# Line Graph Setup
plt.title("South Forty Foot Drain River Level at Boston Black Sluice") 
plt.xlabel("Date")
plt.ylabel("Maximum River Level (m)")
plt.grid(color = "green", linestyle = "--", linewidth = 0.5)  # Sets the grid up. Thin green dashed lines on both axis.
plt.plot(filteredDf["date"], filteredDf["max_level"], marker="o")  # Plots the points on the graph with a circle marker.

plt.show()  # Opens the graph in a seperate window.