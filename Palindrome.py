n = int(input())

temp = n
rev = 0

while temp:
    rev = (rev*10) + (temp%10)
    temp //= 10

if n == rev:
    print("Entered Number is Palindrome!!")
else:
    print("Number is not palindrome")