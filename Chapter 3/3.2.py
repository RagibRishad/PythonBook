
# Cost of per square inch of a circular pizza
# diameter and price is given
# Size of Pizza should be in diameter
# Cost per square inch is $5

import math

def main():
    d = 20
    cost = 0.063

    r = d/2

    a = math.pi*r**2

    total = a*cost

    print("The TOTAL COST of Pizza is ", round(total, 2))

main()