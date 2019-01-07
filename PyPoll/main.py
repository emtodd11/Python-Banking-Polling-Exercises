import csv
import os
csvpath = os.path.join('election_data.csv')

#read CSV file
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header row
    header = next(csvreader)

    #create variables to start total vote counts and candidate vote counts at 0
    vote_count = 0
    candidate0_votes = 0
    candidate1_votes = 0
    candidate2_votes = 0
    candidate3_votes = 0

    #create list to store candidate names
    candidates = []
    #create a list to store all the votes
    votes = []


    #loop through each row in CSV file
    for row in csvreader:
        #count total number of votes
        vote_count += 1
        #add each unique name to candidate list
        if row[2] not in candidates:
            candidates.append(row[2])
        #add all votes to the votes list
        votes.append(row[2])

    #loop through the votes and tally for each candidate
    for vote in votes:
        if vote == candidates[0]:
            candidate0_votes += 1
        if vote == candidates[1]:
            candidate1_votes +=1
        if vote == candidates[2]:
            candidate2_votes +=1
        if vote == candidates[3]:
            candidate3_votes +=1

    #calculate the percentage of total votes for each candidate
    candidate0_percent = candidate0_votes / vote_count * 100
    candidate1_percent = candidate1_votes / vote_count * 100
    candidate2_percent = candidate2_votes / vote_count * 100
    candidate3_percent = candidate3_votes / vote_count * 100

    #find the winner
    

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {vote_count}")
    print("-------------------------")
    print(f"{candidates[0]}: {candidate0_percent}% ({candidate0_votes})")
    print(f"{candidates[1]}: {candidate1_percent}% ({candidate1_votes})")
    print(f"{candidates[2]}: {candidate2_percent}% ({candidate2_votes})")
    print(f"{candidates[3]}: {candidate3_percent}% ({candidate3_votes})")
    print("-------------------------")
    print(f"Winner: ")
    print("-------------------------")


