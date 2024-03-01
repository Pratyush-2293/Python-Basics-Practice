n = input("Enter a number: ")

def CheckPalindrome(strNum):
    revStrNum = strNum[::-1]
    if(strNum == revStrNum):
        print("The number is palindrome.")
        return

    print("The number is not palindrome.")
    return


CheckPalindrome(n)