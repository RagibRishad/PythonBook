
# 1 pound  = $10.50
# Shipping cost is $0.86 per pound + $1.50 overhead cost
# Calculate shipping cost

import math

def main():
    customer_demand = eval(input("Enter the quantity of pound you want to buy: "))
    per_pound = 10.50*customer_demand
    overhead_cost = 1.50
    shipping_cost = 0.86*customer_demand

    total = per_pound+shipping_cost+overhead_cost

    print("Total Price is: ", round(total))


main()