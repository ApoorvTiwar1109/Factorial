#factorial of a number
#while loop
def factorial(n):
    num = 1
    fac = 1
    while fac<=n:
        num = num * fac
        fac = fac + 1
    return num
number = int(input("Enter number : "))
print(factorial(number))

#for loop (iterative)
def factorial2(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number2 = int(input("Enter number : "))
print(factorial2(number2))  

#if/else (recursive)
def factorial3(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial3(n - 1)
number3 = int(input("Enter number : "))
print(factorial3(number))