
import math

def main():
    x1 = 5
    y1 = 6

    x2 = 8
    y2 = 9

    x = (x2 - x1)**2
    y = (y2 - y1)**2

    distance = x+y

    result = math.sqrt(distance)

    print("DISTANCE is ", round(result, 2))

main()