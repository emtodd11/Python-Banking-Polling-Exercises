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
    winner = 0

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
    candidate0_percent = round(candidate0_votes / vote_count * 100, 3)
    candidate1_percent = round(candidate1_votes / vote_count * 100, 3)
    candidate2_percent = round(candidate2_votes / vote_count * 100, 3)
    candidate3_percent = round(candidate3_votes / vote_count * 100, 3)

    #find the winner
    if candidate0_votes > candidate1_votes and candidate0_votes > candidate2_votes and candidate0_votes > candidate3_votes:
        winner = candidates[0]

    if candidate1_votes > candidate0_votes and candidate1_votes > candidate2_votes and candidate1_votes > candidate3_votes:
        winner = candidates[1]

    if candidate2_votes > candidate0_votes and candidate2_votes > candidate1_votes and candidate2_votes > candidate3_votes:
        winner = candidates[2]

    if candidate3_votes > candidate0_votes and candidate3_votes > candidate1_votes and candidate3_votes > candidate2_votes:
        winner = candidates[3]


    output = "Election Results\n"
    output += "-------------------------\n"
    output += "Total Votes: " + str(vote_count) + "\n"
    output += "-------------------------\n"
    output += str(candidates[0]) + ": " + str(candidate0_percent) + "% (" + str(candidate0_votes) + ")\n"
    output += str(candidates[1]) + ": " + str(candidate1_percent) + "% (" + str(candidate1_votes) + ")\n"
    output += str(candidates[2]) + ": " + str(candidate2_percent) + "% (" + str(candidate2_votes) + ")\n"
    output += str(candidates[3]) + ": " + str(candidate3_percent) + "% (" + str(candidate3_votes) + ")\n"
    output += "-------------------------\n"
    output += "Winner: " + str(winner) + "\n"
    output += "-------------------------\n"

    print(output)

    file = open("Emily_Todd_Python-Challenge_PyPoll.txt","w")
    file.write(output)

    file.close()
