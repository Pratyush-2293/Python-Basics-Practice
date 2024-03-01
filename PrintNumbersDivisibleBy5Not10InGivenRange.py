n = int(input("Enter range: "))

def FindDividendsInRange(num):
    for i in range(num):
        if i % 5 == 0 and i % 10 != 0:
            print(i)

    return


FindDividendsInRange(n)