# Modules
import os
import csv

# Set path for file
csvpath = "Resources/budget_data_Shanara.csv"
txtpath = "analysis/budget_analysis.txt"

# variables
total_months = 0
total_sumpl = 0
changespl = []
last_profit_loss = 0


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header, looping through row by row
    for row in csvreader:
        # print(row)
    
        # add 1 to total months counter
        total_months = total_months + 1
        total_sumpl = total_sumpl + int(row[1])
        
        # calculate the changes in profit/losses
        current_profit_loss = int(row[1])
        change = current_profit_loss - last_profit_loss
        changespl.append(change)
        last_profit_loss = current_profit_loss
            
    
# print out KPIs total number of months in dataset
with open(txtpath, encoding='UTF-8',mode="w") as txtfile:
    output=(
        f"Financial Analysis\n"
        f"----------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: {total_sumpl}\n"
        
    )
    print(output)
    txtfile.write(output)

    
#     Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
