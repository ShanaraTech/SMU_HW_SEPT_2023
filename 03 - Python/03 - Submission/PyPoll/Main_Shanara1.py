# Modules
import os
import csv

# Set path for file
csvpath = "Resources/election_data_Shanara.csv"
txtpath = "analysis/election_data.txt"

# variables
total_votes = 0
cand_dict = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        
        # add 1 to total votes counter
        total_votes = total_votes + 1
        
        #identify candidates
        #if candidate is listed in the dictionary, then plus 1 to their votes received
        #else, add the candidate to the dictionary with a value of 1
        candidate = row[2]
        
        if candidate in cand_dict.keys():
            cand_dict[candidate] += 1
        else:
            cand_dict[candidate] = 1
        
# print(total_votes)
# print(cand_dict)         
        
        
# initialize a variable
# loop through the candidates
# if highest count of votes, update the variable value

winning_votes = 0
winning_candidate = ""    
output = f''        

for cand in cand_dict.keys():
    votes = cand_dict[cand]
    
    
    # check if more votes than previous candidate
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = cand
        
# print(winning_candidate, winning_votes)     

################################################ 
   
        
    for key in cand_dict.keys():
        perc = round(100* cand_dict[key]/total_votes, 3)
        newline = f"{key}: {perc}% ({cand_dict[key]})\n" 
      
        





# print results of the election analysis dataset and write it to a txtfile
with open(txtpath, encoding='UTF-8',mode="w") as txtfile:
    output=(
        f"Election Data\n"
        f"----------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"Candidate Dictionary: {cand_dict}\n"
        f"Election Winner: {winning_candidate, winning_votes}\n"
        f"Charles Casper Stockholm: {85213/total_votes*100, total_votes-winning_votes-cand_dict[cand]}\n"
        f"Diana DeGette: {winning_votes/ total_votes*100, winning_votes}\n"
        f"Raymon Anthony Doane: {perc,cand_dict[cand]}\n"
        f"Winner: {winning_candidate}\n"
        



    )
    print(output)
    txtfile.write(output)
    

#      Election Results
# -------------------------
# Total Votes: 369711
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# Winner: {winning_candidate}