# The data we need to retrieve.
# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
# Windows: Uses a backward slashes to separate folders and files. "\"
# Alt1:  file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file. Variable election data references the file object assigned to the CSV file.
# Alt1:  election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:  
    
    # To do: read and analyze data here.  Recall "reader" function within "csv" module that will read the csv file.
    # alt to do: print(election_data)
    file_reader = csv.reader(election_data)

    # file_reader is referencing the file object stored in memory.  We can iterate through file_reader variable and print each row.
    # print each row in the CSV file.
    # for row in file_reader:
        # print(row)
        # print(row[0]
    # print the header row.
    headers = next(file_reader)
    print(headers)

# Using the open() function with the "w" mode we will write data to the file.
# Alt1: outfile = open(file_to_save, "w")

# In lieu of using open(), use the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    # txt_file.write("Hello World")

    # Write three counties to the file.  Separate by a comma and space.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

    # Write three counties to the file on one line.  One per line.  Use "newline escape sequence" which is \n
    txt_file.write("Counties in the Election\n------------------------------------------\nArapahoe\nDenver\nJefferson")

# Close the file.  Must close file to store data in file!
txt_file.close()

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 