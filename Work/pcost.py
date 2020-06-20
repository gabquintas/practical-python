# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    total_cost = 0
    cost = 0
    for row in rows:
        cost = int(row[1])*float(row[2])
        total_cost += cost

    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
