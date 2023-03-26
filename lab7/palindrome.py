s = input("Enter a String to be checked for Palindrome:")
cp = len(s)//2 # cp - check point
flag = 0
for i in range(cp):
    if s[i] != s[len(s)-i-1]:
        flag = 1
        break

if flag:
    print(f"{s} is not a Palindrome.")
else:
    print(f"{s} is Palindrome.")