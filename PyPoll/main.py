import os
import csv
budget_csv = os.path.join("budget_data.csv")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

