n = int(input("Enter number: "))

def CheckPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False

    return True


def PrimeFactors(num):
    for i in range(1, num+1):
        if num % i == 0 and CheckPrime(i):
            print(i)

    return

PrimeFactors(n)