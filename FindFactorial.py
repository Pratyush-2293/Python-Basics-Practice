n = int(input("Enter a number: "))

def Factorial(num):
    sum = 1

    while(num>0):
        sum = sum * num
        num -= 1

    return sum


print(f"The factorial of {n} is: {Factorial(n)}")