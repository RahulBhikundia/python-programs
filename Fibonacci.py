n = int(input("Enter number of terms for Fibonacci Series to be printed:"))

if n == 1:
    print(1)
elif n == 2:
    print(1,1)
elif n == 0:
    print("Number of terms to be printed is not provided!!")
else:
    print(1,1,end=" ")
    a = 1
    b = 1
    for i in  range(2,n):
        c = a+b
        print(c,end=' ')
        a = b
        b = c