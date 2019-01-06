import csv
import os
csvpath = os.path.join('budget_data.csv')
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    total_months = 0
    total_revenue = 0
    months = []
    revenue = []
    monthly_changes = []

    for row in csvreader:

        total_months = total_months + 1

        total_revenue = total_revenue + int(row[1])

        months.append(row[0])

        revenue.append(row[1])

    for i in range(len(revenue)):

        monthly_changes.append(int(revenue[i]) - int(revenue[i-1]))

        average_change = sum(monthly_changes) / len(monthly_changes)

        greatest_increase = max(monthly_changes)

        greatest_decrease = min(monthly_changes)

        increase_month = months[monthly_changes.index(max(monthly_changes))]

        decrease_month = months[monthly_changes.index(min(monthly_changes))]

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", str(total_months))
    print("Total: $", str(total_revenue))
    print("Average Change: $", str(average_change))
    print("Greatest Increase in Profits: ", increase_month, "$", str(greatest_increase))
    print("Greatest Decrease in Profits: ", decrease_month, "$", str(greatest_decrease))
