"""5. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters."""

def case(string:str)->tuple:
    uc = 0
    lc = 0

    for letter in string:
        if letter.islower():
            lc += 1
        elif letter.isupper():
            uc += 1
    
    return uc,lc

if __name__ == "__main__":
    string = input("Enter a String:")
    u,l = case(string)
    print(f"The number of Upper Case letters in the string: {u}")
    print(f"The number of Lower Case letters in the string: {l}")