import os
import csv
from collections import OrderedDict


def create_profits_per_month_ordered_dict(budget_data_reader):
    """
    """

    profits_per_month_ordered_dict = OrderedDict()

    for row in budget_data_reader:
        date = row[0]
        profit = int(row[1])
        profits_per_month_ordered_dict[date] = profit

    return profits_per_month_ordered_dict


def create_profit_changes_per_month_list(profits_list):
    """
    """

    profit_changes_per_month = [0]

    for i in range(len(profits_list) - 1):
        current_month_profit = profits_list[i]
        next_month_profit = profits_list[i + 1]
        change = next_month_profit - current_month_profit
        profit_changes_per_month.append(change)
    
    return profit_changes_per_month


def calculate_average_change_per_month(profit_changes_per_month_list):
    """Removes first element from "change" list then calculates the average change per month.
    """

    profit_changes_per_month_list_copy = profit_changes_per_month_list.copy()
    del profit_changes_per_month_list_copy[0]
    average_change = sum(profit_changes_per_month_list_copy) / len(profit_changes_per_month_list_copy)

    return average_change


def create_results_string(months_list, profits_list, profit_changes_per_month_list, average_change):
    """
    """

    dollars_template = '${:,.2f}'
    num_of_months = len(months_list)
    total_profit = dollars_template.format(sum(profits_list))
    max_gain_index = profit_changes_per_month_list.index(max(profit_changes_per_month_list))
    max_loss_index = profit_changes_per_month_list.index(min(profit_changes_per_month_list))
    average_change = dollars_template.format(average_change)
    greatest_increase_in_profits = dollars_template.format(profit_changes_per_month_list[max_gain_index])
    greatest_decrease_in_profits = dollars_template.format(profit_changes_per_month_list[max_loss_index])

    results = f"""
    Total Months: {num_of_months} 
    Total: {total_profit}
    Average Change: {average_change} 
    Greatest Increase in Profits: {months_list[max_gain_index]} ({greatest_increase_in_profits})
    Greatest Decrease in Profits: {months_list[max_loss_index]} ({greatest_decrease_in_profits})
    """

    return results


def create_results_txt_file(results):
    """
    """

    f = open('./output/PyBank_Export.txt','w')
    f.write(results)
    f.close()


def main():
    csvpath = os.path.join("..", "PythonChallenge", "data", "budget_data.csv")

    with open(csvpath, newline="") as csvfile:
        budget_data_reader = csv.reader(csvfile, delimiter=",")
        next(budget_data_reader) # Skips the first row/header of csv as to avoid incompatible data-types (e.g. objects & integers)

        profits_per_month_ordered_dict = create_profits_per_month_ordered_dict(budget_data_reader)
        months_list = list(profits_per_month_ordered_dict.keys())
        profits_list = list(profits_per_month_ordered_dict.values())
        profit_changes_per_month_list = create_profit_changes_per_month_list(profits_list)
        average_change = calculate_average_change_per_month(profit_changes_per_month_list)
        average_change_rounded = round(average_change, 2)
        results = create_results_string(months_list, profits_list, profit_changes_per_month_list, average_change_rounded)

        print(results)

        create_results_txt_file(results)


main()