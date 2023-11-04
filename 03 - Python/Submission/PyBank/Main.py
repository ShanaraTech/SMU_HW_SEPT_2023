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


max_change = -9999999999
min_change = 9999999999
max_month = ""
min_month = ""


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header, looping through row by row
    for row in csvreader:
        # print(row)
        
        # Changes in profits and losses
        # if no profit/loss change in first row, let x = 0 or last_profit_loss
        # else, compute the profit/loss change amount
        
        if total_months != 0:
            change = int(row[1]) - last_profit_loss
            changespl.append(change)
            
            # locate the Max & Min change
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
            else:
                pass # leave unchanged & proceed with locating range of values specified 
                

        #  calculate the amount using the previous month's profit/loss 
        last_profit_loss = int(row[1])
        
        # add 1 to total months counter
        total_months = total_months + 1
        
        # Add the variable to the sum of Profit/Losses
        total_sumpl = total_sumpl + int(row[1])
        
        
        

avg_change = sum(changespl) / len(changespl)    
                
    
# show 5 KPI results analyzed using the budget csv financial dataset
with open(txtpath, encoding='UTF-8',mode="w") as txtfile:
    output=(
        f"Financial Analysis\n"
        f"----------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: {total_sumpl}\n"
        f"Average Change: {avg_change}\n"
        f"Greatest Profit Range Increase: {max_change}\n"
        f"Date of Highest Profit Range: {max_month}\n"
        f"Greatest Profit Range Decrease: {min_change}\n"
        f"Date of Lowest Profit Range: {min_month}\n"
        
        
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
