c = input("Enter a character:")

if len(c) != 1:
    print("Invalid! Not a character!!")
    exit()

if c.isupper():
    print(f'{c} is uppercase')
elif c.islower():
    print(f'{c} is lowercase')
else:
    print("Not an alphabet")
