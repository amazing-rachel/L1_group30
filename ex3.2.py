import json
import timeit

# Open and load JSON file
with open("large-file.json", "r", encoding = "UTF=8") as file:
    content = json.load(file)         # Load file data into 'content' variable

# Import/define stuff we'll need for plotting (from provided GitHub link)
import random
import timeit
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]    # Set the default size for the plot
import numpy as np

# Defining the function that changes the size field in every JSON file record to 42 
def change_content(data):
    for i in data:              
        if isinstance(i,dict):               # Check if the element is a dictionary
            if 'payload' in i:                  # Check if the key: 'payload' exists
                if 'size' in i['payload']:          # If the 'size' key exists, set it to 42
                    i['payload']['size'] = 42
                elif 'release' in i['payload']:                 # If 'release' key exists within 'payload'
                    if 'assets' in i['payload']['release']:         # If 'assets' exists in 'release', set 'size' of each asset to 42
                        for j in i['payload']['release']['assets']:
                            j['size'] = 42
                    elif 'repo' in i['payload']['release']:         # If 'repo' exists in 'release', set its 'size' to 42
                        for j in i['payload']['release']['repo']:
                            j['size'] = 42 
                elif 'pull_request' in i['payload']:                     # If 'pull_request' exists in payload
                    if 'head' in  i['payload']['pull_request']:                 # If 'head' exists, set its 'repo' size to 42
                          if 'repo' in i['payload']['pull_request']['head']:
                                repo = i['payload']['pull_request']['head']['repo']
                                if isinstance(repo, dict):
                                    repo['size'] = 42
                                else:
                                    i['payload']['pull_request']['head']['size'] = 42
                    if 'base' in  i['payload']['pull_request']:                           # If 'base' exists, set its 'repo' size to 42
                        if 'repo' in i['payload']['pull_request']['base']:
                            i['payload']['pull_request']['base']['repo']['size'] = 42
                elif 'forkee' in i['payload']:                                            # If 'forkee' exists in 'payload', set its 'size' to 42
                    i['payload']['forkee']['size'] = 42
                            
                    
    return data      # Returned the changed content
              
#elapsed_time = timeit.timeit(lambda: change_content(content), number=10)
#print('The everage time across the ten repetitions is:', elapsed_time/10, 'seconds.')

#changed_content = change_content(content)
#changed_content = changed_content[::-1]
#with open("output.2.3.json", "w") as file:
#   json.dump(changed_content, file, indent=4, separators=(',', ':'))

recordSizes = [1000, 2000, 5000, 10000]         # List of different sizes of records to test

averageTimes = []                       # List to store the average processing times for each tested record size

for size in recordSizes:                                # Iterating through each record size in the list
    print(f"Measuring for first {size} records:")
    dataRecordSized = content[:size]                    # Looking only at the content within a certain 'size' of records
    
    repeat100List = []                                  # List to store times for 100 test repetitions 

    # Measuring the time for 100 repetitions
    for value in range(100):
        elapsedTime = timeit.timeit(lambda: change_content(dataRecordSized), number = 1)        # Measure time for a single repetition
        repeat100List.append(elapsedTime)                                                       # Append the time to the list
    
    averageTime = sum(repeat100List)/len(repeat100List)                                         # Calculate the average time for 100 repetitions
    averageTimes.append(averageTime)                                                            # Appending the average time to the list
    print(f"Average time for list of length {size}: {averageTime} seconds")


# Now, compute linear regression to find the slope and intercept of the line
# that most accurately describes the relationship between input length and time.
# Then, plot the data and the line.

# Apply the linear regression model on the record sizes and average times
slope, intercept = np.polyfit(recordSizes, averageTimes, 1)

# Plotting data points (record sizes vs average times)
plt.scatter(recordSizes, averageTimes)


# Create the line using the linear regression slope and intercept
line = [slope * records + intercept for records in recordSizes]

# Plot the linear regression line in red
plt.plot(recordSizes, line, 'r')

plt.title("Average Processing Time vs. Number of Records")
plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (in seconds)")

plt.savefig("output.3.2.png")

print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))