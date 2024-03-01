n = int(input("Enter number: "))

def CountDigits(num):
    strnum = str(num)
    return len(strnum)


print(f"Number of digits in {n} is: {CountDigits(n)}")