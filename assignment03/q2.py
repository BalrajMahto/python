#factorial of a number

n=int(input("enter a no.:  "))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("the factorial is :",factorial(n))
