
with open("pg2701.txt", "r", encoding= "UTF-8") as file:     # Open the file "pg2701.txt" in read mode
    lines = file.readlines()                                 # Read all lines from the file into a list

lines = [line.strip() for line in lines]                     # Remove leading and trailing whitespace

vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]    # List of vowel characters

wordCount = 0                                       # Initializing a counter variable for the total number of words in the text
vowelCount = 0                                      # Initializing a counter variable for the total number of vowels in the text


for line in lines[40 :]:                            # Looping through each line starting from the 40th line
    wordCount = wordCount + len(line.split())       # Counting the number of words in the current line by splitting line at spaces and adding to wordCount
    for char in line:                               # Looping through each character in the line
        if char in vowels:                          # Check whether the character is in the list of vowels
            vowelCount = vowelCount + 1             # Increment the vowel counter variable if the character is a vowel


print("The average number of vowels per word in the text is: ", vowelCount/wordCount)