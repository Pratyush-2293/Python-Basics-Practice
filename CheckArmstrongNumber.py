n = input("Enter a number to check: ")

def CheckArmstrong(strNum):
    num = int(strNum)
    original = num
    order = len(strNum)
    sum = 0

    while(num>0):
        digit = num % 10
        sum += digit ** order
        num = num // 10

    if(sum == original):
        print("This is an Armstrong number.")
        return

    print("This is not an Armstrong number.")


CheckArmstrong(n)