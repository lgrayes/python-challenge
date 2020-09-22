#Begin
import os
import csv

#Set file paths
poll_csv = os.path.join("election_data.csv")
output_path = os.path.join("..", "Analysis", "new.csv")

# #Read csv file
with open(poll_csv) as csvfile:
    csv_Reader = csv.reader(csvfile)
    header = next(csv_Reader)
    # print(header)

    #Set start of reading columns
    totalVotes = 0
    PctVoteCand = 0
    TotalVoteCand = 0
    val = 0
    
    #Set start in counting rows
    for row in csv_Reader:
    # totalRowCount.append(totalRows)
        VoterID = str(row[1])
        val = int(row[2])
        Candidate = str(row[3])
    #     total = total + val
    #     totalRows = len(budget_csv)
    #     average = total / totalRows
        KhanCount = 0

        if(Candidate == 'Khan'):
            KhanCount = KhanCount + val
    #     if((val< 0 ) and val < lowestProfit):
    #         lowestProfit = val

print ("_____________________________")
print ("Election Results")
print ("_____________________________")
# print (f"Total Number of Votes Cast: {totalVotes}")
print ("_____________________________")
# print (f"Khan: {KhanCount}")
# print (f"Complete List of candidates who received votes: {ListofCandidates}")
# print (f"Percentage of votes each candidate won: {PctVoteCand}")
# print (f"Total number of votes each candidate won:  {TotalVoteCand}")
print ("_____________________________")
# print (f"Winner of election based on popular votes:  {Winner}")
print ("_____________________________")

# output to Analysis/csv folder
# with open(output_path, 'w') as csvfile:
    # csvwriter = csv.writer(csvfile, delimiter=',')
    # csvwriter.writerow(['Total Months'])
