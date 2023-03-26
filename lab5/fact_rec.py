"""3. Write a Python function to calculate the factorial of a number (a non-negative integer). The
function accepts the number as an argument."""

def fact(num):
    if num == 0:                # Terminating Condition
        return 1
    
    return num * fact(num-1)    # Recursive call

if __name__ == "__main__":
    num = int(input("Enter a number:"))
    print(f'{num}! = {fact(num)}')