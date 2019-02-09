import os
import csv
from collections import OrderedDict

csvpath = os.path.join("..", "python-challenge", "Pybank", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips the first row/header of csv as to avoid incompatible data-types (e.g. objects & integers)
    next(csvreader)
    bank = OrderedDict()
    change = [0]

    #creates key-value pairs for each row in the first and second columns (for "bank" dictionary).
    for every_row in csvreader:
        #each key is a date  #each value is the profit for that date.
        bank[every_row[0]] = int(every_row[1])

    #indexes bank dictionary, then appends the difference between indexes into "change" list.
    for i in range(len(bank.values())):
      if i == len(bank.values()) - 1:
        break
      else:
        change.append(list(bank.values())[i+1] - list(bank.values())[i])

    #removes first element from "change" list then calculates the average.
    def avr_change():
      change2 = change.copy()
      del change2[0]
      avr_change = sum(change2) / len(change2)
      return avr_change

        
    num_of_months = len(bank.keys())
    total = sum(bank.values())
    max_gain = change.index(max(change))
    max_loss = change.index(min(change))
    results = (f"Total Months: {num_of_months} \nTotal: ${total} \nAverage Change: ${round(avr_change(), 2)} \nGreatest Increase in Profits: {list(bank.keys())[max_gain]} (${change[max_gain]})\nGreatest Decrease in Profits: {list(bank.keys())[max_loss]} (${change[max_loss]})")

    print(results)

f = open('PyBank_Export.txt','w')
f.write(results)
f.close()
