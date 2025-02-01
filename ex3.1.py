import matplotlib.pyplot as plt
import numpy as np

import json
with open("internetdata.json", "r", encoding="utf-8") as file:
    data = json.load(file)

countriesUnder10000 = []
countriesAtAndOver10000 = []

for entry in data:
    if entry["incomeperperson"] is not None:
        if entry["incomeperperson"] < 10000:
            countriesUnder10000.append(entry)
        else:
            countriesAtAndOver10000.append(entry)

countryAtAndOver10000List = []
countryUnder10000List = []

for country in countriesAtAndOver10000:
    countryAtAndOver10000List.append(country["country"])

for country in countriesUnder10000:
    countryUnder10000List.append(country["country"])

atAndOver10000InternetUsage = []
under10000InternetUsage = []

for country in countriesAtAndOver10000:
    atAndOver10000InternetUsage.append(country["internetuserate"])

for country in countriesUnder10000:
    under10000InternetUsage.append(country["internetuserate"])


# Histogram for countries with income under 10000
plt.figure()
under10000 = [rate for rate in under10000InternetUsage if rate is not None]

plt.hist(under10000)

plt.xlabel("Internet Usage Rate")
plt.ylabel("Number of Countries")
plt.title("Histogram of Internet Usage (For Countries with Income < 10000)")

plt.show
plt.savefig("hist1.png")


# Histogram for countries with income at and over 10000
plt.figure()
over10000 = [rate for rate in atAndOver10000InternetUsage if rate is not None]

plt.hist(over10000)

plt.xlabel("Internet Usage Rate")
plt.ylabel("Number of Countries")
plt.title("Histogram of Internet Usage (For Countries with Income ≥ 10000)")

plt.show
plt.savefig("hist2.png")


