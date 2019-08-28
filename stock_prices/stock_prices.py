#!/usr/bin/python

import argparse

#                               REQUIREMENTS
#   1.) Takes a list of stock prices
#   2.) Will return maximum profit from the sale and purchase of one the stock prices
#   3.) Want to find the maximum difference between the smallest and largest prices
#   4.) Max profit can only be computed by subtracting a price by another price
#       that comes before it in the list of prices
#   5.) Keep track of max profit so far and min price so far

#                                Steps to take
#   1.) subtract arr[1] - arr[0]
#   2.) subtract arr[2] - arr[1]
#   3.) subtract arr[2] - arr[0]
#   4.) subtract arr[3] - arr[2]
def find_max_profit(prices):
    # prices = [list of stock prices]
    max_profit_so_far = None

    for price in prices:
        for subtracting_number in range(0, prices.index(price)):
            result = price - prices[subtracting_number]
            if max_profit_so_far == None or result > max_profit_so_far:
                max_profit_so_far = result
    return max_profit_so_far





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))