strNumbers = input("Enter numbers separated by space: ")
strNumberList = strNumbers.split()
numberList = []

for i in strNumberList:
    numberList.append(int(i))

totalSum = sum(numberList) # built in sum function
average = totalSum / len(numberList)

print(f"The sum of given numbers is: {totalSum}")
print(f"The average of given numbers is: {average}")