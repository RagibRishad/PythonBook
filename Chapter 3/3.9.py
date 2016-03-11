
import math

def main():
    a = 10
    b = 11
    c = 12

    s = (a+b+c)/2

    root = s*(s-a)*(s-b)*(s-c)

    A = math.sqrt(root)

    print("The area of a triangle is: ", round(A, 2))

main()

