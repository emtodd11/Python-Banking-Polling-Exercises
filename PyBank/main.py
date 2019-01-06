import csv
import os
csvpath = os.path.join('budget_data.csv')
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    total_months = 0
    total_revenue = 0
    revenue = []
    monthly_changes = []

    for row in csvreader:

        total_months = total_months + 1

        revenue.append(row[1])

        total_revenue = total_revenue + int(row[1])

    for i in range(1,len(revenue)):

        monthly_changes.append(int(revenue[i]) - int(revenue[i-1]))

        average_change = sum(monthly_changes) / len(monthly_changes)

        greatest_increase = max(monthly_changes)

        greatest_decrease = min(monthly_changes)



    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", str(total_months))
    print("Total: $", str(total_revenue))
    print("Average Change: $", str(average_change))
    print("Greatest Increase in Profits: ", "$", str(greatest_increase))
    print("Greatest Decrease in Profits: ", "$", str(greatest_decrease))
