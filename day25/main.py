"""
import csv

with open("./weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))
    print(temperatures)
"""

import pandas