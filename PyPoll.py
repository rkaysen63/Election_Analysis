# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 

# The data we need to retrieve.
# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
# Windows: Uses a backward slashes to separate folders and files. "\"
# Alt1:  file_to_load = 'Resources/election_results.csv'
file_to_load = "C:\\Users\\kayse\\OneDrive\\Documents\\GitHub\\Election_Analysis\\Resources\\election_results.csv"
# file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.  This is the accumulator variable.
#  We need to do this before we open the file because we want total_votes to reset to zero before we run it.
total_votes = 0

# Declare a new list
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. Variable election data references the file object assigned to the CSV file.
# Alt1:  election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:  
    
    # practice to do: print(election_data), output is everything and it's alot!

    # To do: read and analyze data here.  Recall "reader" function within "csv" module that will read the csv file.
    # file_reader is referencing the file object stored in memory.  We can iterate through file_reader variable and print each row.
    file_reader = csv.reader(election_data)
    
    # Read the header row. ??
    headers = next(file_reader)
    
    # print each row in the CSV file,  print(row) or print a comma separated value in the row, print(row[2])
    for row in file_reader: 
        # print(row)
        # print(row[0]
        # Add to the total vote count.  Std py format number = number + 1 augmented to number += 1
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add candidate's name to the candidate list. i.e append candidate_options 
        # But we only want the candidate's name one time.
        # If the candidate does not match any existing candidate..
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# Save the results to the text file.
## Alt1: outfile = open(file_to_save, "w")
# In lieu of using open(), use the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # 3  Print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(candidate_results)
        # Save candidate results to the text file
        txt_file.write(candidate_results)

        # 5. Determine winning vote count, winning percentage, and candidate
        # Determine if the votes are greater than the winning count. Starts at zero.  
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print the winning candidate's results to the terminal outside of if or will stop on first candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

# Close the file.  Must close file to store data in file!
txt_file.close()

