
# Count the number of seconds that pass between a flash of lightning and the crack of thunder that follows it
# Divide that number by five
# The resulting number will tell you how many miles away you are from where lightning just struck.

import math

def main():
    s = eval(input("Number of Seconds of flash and sound: "))

    d = s/5

    print("You are", d, "miles away from Lightning.")

main()