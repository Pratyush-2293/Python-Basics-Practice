n = int(input("Enter a range: "))

def PrintPrimeNumbers(num):
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

    return


PrintPrimeNumbers(n)