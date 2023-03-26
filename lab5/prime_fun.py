"""4. Write a Python function that takes a number as a parameter and check the number is prime or not."""

def isprime(num:int)->bool:
    """A function that takes a number as a parameter and check the number is prime or not."""
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    num = int(input("Enter a number:"))
    
    if isprime(num):
        print(f'{num} is a Prime Number.')
    else:
        print(f'{num} is NOT a Prime Number.')