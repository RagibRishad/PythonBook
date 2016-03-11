
# Future value
# principal amount
# annual percentage rate
# repeat 10 times

def main():
    principal = eval(input("Amount to invest each year: "))
    apr = eval(input("Interest Rate: "))
    yr = eval(input("Years: "))

    for i in range(yr):
        principal = principal * (1 + apr)

        print("Future Value for year", end = " ")
        print(i+1, end = " ")
        print("is ", principal)

main()