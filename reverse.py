n = int(input("Enter a number:"))

temp = n
rev = 0
while temp:
    rev = (rev*10) +(temp%10)
    temp //= 10

print(f'Reverse of {n} is {rev}')