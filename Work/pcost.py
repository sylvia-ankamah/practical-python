# pcost.py
#
# Exercise 1.27
total_cost = 0
f=open('Data/portfolio.csv', 'rt') 

with f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares= int(row[1])
        price = float(row[2])
        total_cost += nshares * price

print('Total cost', total_cost)

#Exercise 1.33
import csv
def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    f=open('Data/portfolio.csv', 'rt')

    with f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            
            except ValueError:
                print('Bad row:', row)

    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
