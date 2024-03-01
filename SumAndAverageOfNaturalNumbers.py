n = int(input("Enter number: "))

def FindSum(num):
    total = 0
    for i in range(1,n+1):
        total += i

    return total


def FindAverage(sum, n):
    return sum/n

totalSum = FindSum(n)
print(f"The sum of first {n} natural numbers is: {totalSum}")
print(f"The average of first {n} natural numbers is: {FindAverage(totalSum, n)}")