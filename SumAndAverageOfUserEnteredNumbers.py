numbers = input("Enter numbers separated by space: ")
numList = numbers.split()

def FindSum(numList):
    total = 0
    for i in numList:
        total += int(i)

    return total


def FindAverage(total, n):
    return total/n


totalSum = FindSum(numList)
print(f"The sum of given numbers is: {totalSum}")
print(f"The average of given numbers is: {FindAverage(totalSum, len(numList))}")