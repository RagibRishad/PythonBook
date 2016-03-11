
import math

def main():
    height = eval(input("Enter height of the wall: "))

    radian = math.pi/180

    length = height/math.sin(radian)

    print("The Length of the ladder should be ", round(length, 2))

main()