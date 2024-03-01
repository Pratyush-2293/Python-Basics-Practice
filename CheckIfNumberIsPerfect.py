n = int(input("Enter a number: "))

def CheckPerfect(num):
    divisorList = []
    for i in range(1,num):
        if num % i == 0:
            divisorList.append(i)

    sum = 0
    for j in divisorList:
        sum += j

    if(sum == num):
        print("The number is perfect.")
        return

    print("The number is not perfect.")
    return


CheckPerfect(n)