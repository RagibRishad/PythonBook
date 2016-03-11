
def main():

    celcius = eval(input("Write temp: "))

    for i in range(celcius, 110, 10):
        fahrenheit = 9/5 * i + 32
        print(i, "means", fahrenheit, "fahrenheits")

main()