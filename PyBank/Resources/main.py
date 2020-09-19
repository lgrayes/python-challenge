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
    total = 0

    #Set start in counting rows
    for row in csv_Reader:
        val = int(row[1])
        total = total + val
        if((val > 0) and val > highestProfit):
            highestProfit = val
        #if((val< 0 ) and ):        

# #Define columns for calculations
# def calculations(budgetData):
# date=int(budgetData[1])
# Profit=int(budgetData[2])

# #Calculate sum
# #Calculate average
# def average(budgetData):
# 	sum = 0
# 	for number in budgetData:
# 		sum = sum + number

# 	average_of_those_numbers = sum/len(budgetData)

# #Try this 2nd calculation for average
# average_of_those_numbers = average


# #Gather highest and lowest profit numbers to print
# for x in column 2
# if startProfit > 0 then
# 	highestProfit = startProfit + highestProfit
# else
# 	lowestProfit = startProfit + lowestProfit


print ("_____________________________")
print ("Financial Analysis")
print ("_____________________________")
print ("Total Months: ")
print (f"Total: {total}")
# print (f”Average Change: {average_of_those_numbers}”)
print (f"Greatest Increase in Profits:  {highestProfit}")
# print (f”Greatest Decrease in Profits: ” {lowestProfit})