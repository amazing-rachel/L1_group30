import matplotlib.pyplot as plt
import numpy as np

import json
with open("internetdata.json", "r", encoding="utf-8") as file:
    data = json.load(file)                      # Load the data from the file into the data list

countriesUnder10000 = []                        # Countries with income per person under 10000
countriesAtAndOver10000 = []                    # Countries with income per person equal to or greater than 10000


# Classifing countries based on their income per person and appending them to the appropriate lists
for entry in data:
    if entry["incomeperperson"] is not None:        # Make sure the income per person is not None
        if entry["incomeperperson"] < 10000:        # If income is less than 10000
            countriesUnder10000.append(entry)       # Add this country to list: 'countriesUnder10000'
        else:
            countriesAtAndOver10000.append(entry)   # Add this country to list 'countriesAtAndOver10000' 

countryAtAndOver10000List = []                      # List to store country names with income >= 10000
countryUnder10000List = []                          # List to store country names with income < 10000


# Append country names to lists based on income 

for country in countriesAtAndOver10000:                     # For each country in the list of countries with income >= 10000
    countryAtAndOver10000List.append(country["country"])    # Append the country name to the list

for country in countriesUnder10000:                         #For each country in the list of countries with income < 10000
    countryUnder10000List.append(country["country"])        # Append the country name to the list


# Initialize lists to store the internet usage rates for each category:
atAndOver10000InternetUsage = []
under10000InternetUsage = []


# Add to appropriate list the internet usage rates for each country based on income:
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


