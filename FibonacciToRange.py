n = int(input("Enter number of terms: "))

def PrintFibonacci(num):
    a = 0
    b = 1

    # initial numbers
    print(a)
    print(b)

    for i in range(num-2):
        c = a+b
        print(c)
        a = b
        b = c

    return

PrintFibonacci(n)