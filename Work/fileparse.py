# fileparse.py
#
# Exercise 3.4
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for
            colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            if indices:
                row = [ row[index] for index in
                indices ]
            
            if types:
                 row = [func(val) for func, val in zip(types, row) ]


            record = dict(zip(headers, row))
            records.append(record)

    return records

shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
print(shares_held)  
