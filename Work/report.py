# report.py
#
# Exercise 2.4
import csv
import os

def read_portfolio(filename):
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        next(f) # Skip header
        for row in rows:
            stock = {
                    'name'   : row[0],
                    'shares' : int(row[1]),
                    'price'   : float(row[2])
                        }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices ('Data/prices.csv')

current_value = 0.0
gain_or_loss = 0.0

for s in portfolio:
    current_value += s['shares'] * s['price']
    gain_or_loss = (s['price'] - prices.get(s['name'])) * s['shares']

print(f'Portfolio Current Value: ${current_value:0.2f}')
print(f'Gain / Loss: ${gain_or_loss:0.2f}')
