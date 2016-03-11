#converting celsius into fahrenheit 5 times

def check():
    celcius = eval(input("Write down the temperature in Celsius: "))
    fahrenheit = 9/5 * celcius + 32

    for i in range(5):
        print("The temperature is", fahrenheit, "fahrenheits")

check()