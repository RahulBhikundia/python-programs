c = input("Enter a character:")

if len(c) != 1:
    print("Invalid! Not a character!!")
    exit()

vowel = {'a','e','i','o','u','A','E','I','O','U'}
if c in vowel:
    print(c,"is a vowel")
elif (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
    print(c,"is a Consonant")
else:
    print("Not a character")
