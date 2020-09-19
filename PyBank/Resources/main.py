#Begin
import os
import csv

#Set file paths
#THANK YOU TO MO FOR THE HELP
budget_csv = os.path.join("budget_data.csv")
output_path = os.path.join("..", "Analysis", "new.csv")

# #Read csv file
with open(budget_csv) as csvfile:
    csv_Reader = csv.reader(csvfile)
    header = next(csv_Reader)
    # print(header)

    #Set start of reading Profits column
    startProfit = 0
    highestProfit = 0
    lowestProfit = 0
    totalRows = 0
    total = 0
    average = 0

    #Set start in counting rows
    for row in csv_Reader:
        val = int(row[1])
        total = total + val
        totalRows = len(budget_csv)
        average = total / totalRows

        if((val > 0) and val > highestProfit):
            highestProfit = val
        if((val< 0 ) and val < lowestProfit):
            lowestProfit = val

print ("_____________________________")
print ("Financial Analysis")
print ("_____________________________")
print (f"Total Months: {totalRows}")
print (f"Total: ${total}")
print (f"Average Change: ${average}")
print (f"Greatest Increase in Profits:  {highestProfit}")
print (f"Greatest Decrease in Profits:  {lowestProfit}")

# output to Analysis/csv folder
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Months'])
