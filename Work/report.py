# report.py
#
# Exercise 2.11
import csv
def read_portfolio(filename):
    '''Read in the holdings from a portfolio'''
    portfolio= []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0],
            'shares': int(row[1]), 
            'price': float(row[2])
            }
            portfolio.append(holding)
            
    return portfolio


def read_prices(filename):
    prices = {}

    f= open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        try:

             prices[row[0]] = float(row[1])
        except IndexError:
            pass

    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
current_value = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']
    current_value += s['shares']*prices[s['name']]

print('Total cost:', total_cost)
print('Current value:', current_value)
print('Gain/Loss:', current_value - total_cost)

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
        
report = make_report_data(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
    