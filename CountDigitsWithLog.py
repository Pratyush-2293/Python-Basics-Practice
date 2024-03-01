import math

n = int(input("Enter number: "))

def CountIntegers(num):
    return math.floor(math.log10(num)+1)


print(f"The number of digits in {n} are: {CountIntegers(n)}")