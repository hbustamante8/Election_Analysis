import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1 Initialzie the vote counter
total_votes = 0
# create candidate option before the while loop
candidate_options = []
# create candidate vote options
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
   

#print each row in the CSV file

    for row in file_reader:
    #2. Add to the total vote count.
        total_votes += 1
        #if the candidate_name does not match any existing candidate

        candidate_name = row[2]
        if candidate_name not in candidate_options:
            
        #Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)
            
        # Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve the vote count of candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        vote_percentage = float(votes)/ float(total_votes)*100
        
        # Print out candidates name, vote count, and percentage 
        print(f' {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    #determine winning vote count and candidate 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
    # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes 
            winning_percentage = vote_percentage
    # Set the winning candidate equal to the candidates name 
            winning_candidate = candidate_name
    
    #print winning candidate summary

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



#3 Print the total votes
#print(total_votes)

#print the candidate list 
#print(candidate_options)
#print(candidate_votes)



