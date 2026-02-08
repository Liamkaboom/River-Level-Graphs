import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("CSV/black-sluice-ps-boston-lincolnshire-070226.csv") # Read Comma Separated Value (CSV) file for station data.
df["date"] = pd.to_datetime(df["date"])  # Date column (currently text strings in csv file) --> datetime 

startDate = "2025-01-01"  # Start Date variable (For this file, not by user input as this analyses river levels/flooding from January last year - Jan 1st to Jan 15th 2025)
endDate = "2025-01-15"  # End Date variable (For this file, not by user input as this analyses river levels/flooding from January last year - Jan 1st to Jan 15th 2025)

filteredDf = df[(df["date"] >= startDate) & (df["date"] <= endDate)]  # Goes through every... single... row... in the csv file and filters the dates between the startDate and endDate variables (In this case 2025-01-01 to 2025-01-15, to see the  maximum river levels around when the South Forty Foot flooded.)

# Line Graph Setup
plt.title("South Forty Foot Drain River Level at Boston Black Sluice - January 2025 Flood")
plt.xlabel("Date")
plt.ylabel("Maximum River Level (m)")
plt.grid(color = "green", linestyle = "--", linewidth = 0.5)  # Sets the grid up. Thin green dashed lines on both axis.
plt.plot(filteredDf["date"], filteredDf["max_level"], marker="o") # Plots the points on the graph with a circle marker.

plt.axvspan(pd.Timestamp("2025-01-07 00:00:00"), ("2025-01-07 00:00:00"), color = "red", label = "Date of Flood (Happened just after midnight).")  # Creates a red line on the date of the flood...
plt.legend()  # Creates the Legend so it is clear the red line is for the date of flooding...

plt.show()  # Opens the graph in a seperate window.