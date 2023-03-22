import os
import csv
#store number of votes and candidates 
votes = []
candidates = []
unique_candidates = []
#create variables
stockham = 0
deGette = 0
doane = 0
#path to the csv file
poll_csv = os.path.join("PyPoll","Resources","election_data.csv")
#read the csv file
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#skip the first row
    next(csvreader)
#start for loop to go through rows
    for row in csvreader:
#create 2 lists:votes and all candidates
        votes.append(row[0])
        candidates.append(row[2])
#create a list of candidates who recieved votes
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
#zip 2 lists to calculate how many votes each candidate recieved
    x=zip(candidates,votes)
    for i in x:
       if i[0] =="Charles Casper Stockham":
           stockham=stockham+1
       elif i[0]=="Diana DeGette":
           deGette=deGette+1
       else:
           doane = doane+1
#zip lists to find the MAX value of votes and the winner
Winner = zip([stockham,deGette,doane],unique_candidates,)
#calculate percentage of votes for each candidate
stockham_percent= ("{:.3%}".format(stockham/len(votes)))
deGette_percent = ("{:.3%}".format(deGette/len(votes)))
doane_percent = ("{:.3%}".format(doane/len(votes)))
#print values
print(f"Total Votes: {len(votes)}")
print(f"Charles Casper Stockham: {stockham_percent} ({stockham})")
print(f"Diana DeGette: {deGette_percent} ({deGette})")
print (f"Raymon Anthony Doane: {doane_percent } ({doane})")
print(f"Winner: {max(Winner)[1]}")
