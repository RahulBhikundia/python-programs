n = int(input("Enter Number of terms of Fibonacci Series to be printed:"))

if(n<1):
    print("Invalid! Wrong Input")
elif n == 1:
    print(0)
elif n == 2:
    print("0 1")
else:
    a = 0
    b = 1
    print(a,b,end=' ')
    for i in range(2,n):
        c = a+b
        print(c,end=' ')
        a = b
        b = c