n = input("Enter a number: ")

def ReverseNumber(strNum):
    reverseStrNum = strNum[::-1]
    reversedNum = int(reverseStrNum)
    return reversedNum

print(f"Reverse number is: {ReverseNumber(n)}")