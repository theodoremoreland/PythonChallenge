import os
import csv
from collections import OrderedDict

csvpath = os.path.join("..", "PythonChallenge", "data", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skips the first row/header of csv as to avoid incompatible data-types (e.g. objects & integers)
    next(csvreader)
    profits_per_month = OrderedDict()
    change = [0]

    # Creates key-value pairs for each row in the first and second columns (for "profits_per_month" dictionary).
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        profits_per_month[date] = profit

    months = list(profits_per_month.keys())
    profits = list(profits_per_month.values())
    
    for i in range(len(profits) - 1):
        current_month_profit = profits[i]
        next_month_profit = profits[i + 1]
        change.append(next_month_profit - current_month_profit)

    
    def determine_average_change():
      """Removes first element from "change" list then calculates the average.
      """
      change2 = change.copy()
      del change2[0]
      average_change = sum(change2) / len(change2)
      return average_change

        
    num_of_months = len(months)
    total = sum(profits)
    max_gain = change.index(max(change))
    max_loss = change.index(min(change))
    results = f"""
    Total Months: {num_of_months} 
    Total: ${total}
    Average Change: ${round(determine_average_change(), 2)} 
    Greatest Increase in Profits: {months[max_gain]} (${change[max_gain]})
    Greatest Decrease in Profits: {months[max_loss]} (${change[max_loss]})
    """

    print(results)

f = open('./output/PyBank_Export.txt','w')
f.write(results)
f.close()
