# fibonnaci series
def fib(n):
    c=0
    if n==1:
        c=0
        return c
    elif n==2:
        c=1
        return c
    else:
        c=fib(n-1)+fib(n-2)
        return c
# factorial 
def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
    
    
n=int(input('Enter number:'))
a=input("Enter ! or f:")
if a=='!':
    print(fac(n))
elif a =="f":
    print(fib(n))





