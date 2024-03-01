n = int(input("Enter a number: "))

def FindFactors(num):
    for i in range(1, num):
        if num % i == 0:
            print(i)

    return


FindFactors(n)