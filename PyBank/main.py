#1.Total number of months included in the dataset
import os
import csv
#store number of months
months  = []
#store net total amount
net_total_amount = []
#store deltas
deltas = []
#store dates
dates = []
#create variables for rows for a conditional
currentRow = 0
prevRow = 0
isFirstRow = True
#path to the csv file
budget_csv = os.path.join("PyBank","Resources", "budget_data.csv")
#read the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#skip the first row
    next(csvreader)
#start for loop to go through rows
    for row in csvreader:
#conditional to subtract values of the previous rows from the following ones
       if(isFirstRow==True):
#setting value for the first row
            prevRow =int(row[1])
            isFirstRow = False
       else:
#setting a value for the current row
            currentRow = int(row[1])-prevRow 
#adding deltas to the counter
            deltas.append(currentRow)
#adding dates to the counter
            dates.append(row[0])
#setting value for the previous row for the next loops
            prevRow = int(row[1])
#count the number of rows in column A
       months.append(row[0])
#count the net total amount in column B
       net_total_amount.append(int(row[1]))
#count the length of the months list
total_months=len(months)
#setting variable for total deltas
total_deltas = 0
for delta in deltas:  
        total_deltas = total_deltas + delta
#zip dates and deltas
change = zip(dates,deltas)
for i in change:
    highest_profit=max(deltas)
    highest_loss=min(deltas)
change = zip(dates,deltas)
for i in change:
    if i[1]== highest_profit:
       highest_profit_date = i[0]
    if i[1]== highest_loss:
       highest_loss_date = i[0]
#PRINT ALL OUTCOME
#print total number of months
print(f"Total Months: {total_months}")
#sum and print the values for net total net amount
net_total_amount = sum(net_total_amount)
print(f"Total: ${net_total_amount}")
#calculate average change by dividing the sum of deltas(total deltas) by the number of deltas(len)
# round the number and adding $
#print
averageChange = round(total_deltas/len(deltas),2)
print(f"Average Change: ${averageChange}")
#print greatest increase and decrease in profits
print(f"Greatest Increase in Profits: {highest_profit_date} (${highest_profit})")
print(f"Greatest Decrease in Profits: {highest_loss_date} (${highest_loss})")


         