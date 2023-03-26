import math
def isprime(num:int)->bool:
    if num<1:
        return False
    elif num % 2 == 0:
        return num == 2
    
    for i in range(3,int(math.sqrt(num))):
        if num % i == 0:
            return False
        
    return True

n = int(input("Enter a number to be checked for prime:"))

if isprime(n):
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')