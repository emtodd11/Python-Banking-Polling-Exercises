import csv
import os
csvpath = os.path.join('budget_data.csv')

#read CSV file
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #ignore header row
    header = next(csvreader)

    total_months = 0
    total_revenue = 0

    #create lists for months, revenue, and monthly revenue changes
    months = []
    revenue = []
    monthly_changes = []

    #loop through the CSV rows
    for row in csvreader:
        #count total months
        total_months = total_months + 1
        #sum total revenue
        total_revenue = total_revenue + int(row[1])
        #add each month to the month list
        months.append(row[0])
        #add each revenue amount to the revenue list
        revenue.append(row[1])

    #loop through the list of revenues to find the monthly changes
    for i in range(len(revenue)):
        #add each monthly change to the list
        monthly_changes.append(int(revenue[i]) - int(revenue[i-1]))
        #calculate average monthly change
        average_change = sum(monthly_changes) / len(monthly_changes)
        #calculate max monthly change
        greatest_increase = max(monthly_changes)
        #calculate min monthly change
        greatest_decrease = min(monthly_changes)
        #find the corresponding months for max and min
        increase_month = months[monthly_changes.index(max(monthly_changes))]
        decrease_month = months[monthly_changes.index(min(monthly_changes))]

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", str(total_months))
    print("Total: $", str(total_revenue))
    print("Average Change: $", str(average_change))
    print("Greatest Increase in Profits: ", increase_month, "$", str(greatest_increase))
    print("Greatest Decrease in Profits: ", decrease_month, "$", str(greatest_decrease))
