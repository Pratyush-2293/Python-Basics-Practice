a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def GCD(a, b):
    gcd = 1
    smallerNum = 0
    if a > b:
        smallerNum = b
    else:
        smallerNum = a

    for i in range(1,smallerNum+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


print(f"The GCD of {a} and {b} is {GCD(a,b)}")