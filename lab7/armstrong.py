def isarmstrong(n:int)->bool:
    if n<1:
        return False
    count = 0
    temp = n
    while(temp):
        temp = temp//10
        count += 1
    
    sum = 0
    temp = n
    while temp:
        sum += ((temp%10)**count)
        temp//=10
    
    if sum == n:
        return True
    return False

num = int(input("Enter a number to be checked for Armstrong Number:"))
if isarmstrong(num):
    print(f'{num} is Armstrong Number.')
else:
    print(f'{num} is not an Armstrong Number.')