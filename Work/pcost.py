# pcost.py
#
# Exercise 2.16(a)
import csv
def portfolio_cost(filename):
    
    total_cost = 0.0

    with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Data/portfolio.csv', 'rt')

cost = portfolio_cost(filename)
print('Total cost:', cost)

