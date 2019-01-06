import csv
import os
csvpath = os.path.join('election_data.csv')
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    #print(csv_header)

    vote_count = 0

    for row in csvreader:

        vote_count += 1

    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", str(vote_count))
    print("-------------------------")


