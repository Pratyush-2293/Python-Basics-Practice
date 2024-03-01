n = int(input("Enter number: "))

def CountDigits(num):
    count = 0
    while(num>0):
        num = num//10
        count += 1

    return count


print(f"Digits in number {n} are: {CountDigits(n)}")