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
              
size = 1000         # First 1000 records to test

print(f"Measuring for first {size} records 1000 times...")
dataRecordSized = content[:size]                    # Looking only at the content within a certain 'size' of records

elapsedTimeList = timeit.repeat(lambda: change_content(dataRecordSized), repeat = 1000,number = 1)        # Measure time of 1000 times using repeat function
print("Done.")

# Now, use the time list as the data source to create histogram


plt.hist(elapsedTimeList, bins=30, edgecolor='black')  
plt.xlabel("Processing Time (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Processing Time")
plt.grid(True)
plt.savefig("output.3.3.png")
plt.show()