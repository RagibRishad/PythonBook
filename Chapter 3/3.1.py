#calculate volume and surface of a sphere

import math

def main():
    r = eval(input("Write the radius of the sphere: "))

    v = 4/3*math.pi*r**3

    a = 4*math.pi*r**2

    print("The VOLUME of a Sphere: ", round(v, 2), "and the AREA of a Sphere: ", round(a, 2))

main()