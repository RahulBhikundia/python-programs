"""2. Write a Python program to reverse a string.
Sample String: "1234abcd"
Expected Output: "dcba4321" """

def rev(string)->str:
    """A Python program to reverse a string."""
    string = list(string)
    result = ""
    for i in range(len(string)):
        result += string[len(string)-i-1]
    
    return result

if __name__ == "__main__":
    string = input("Enter s string:")
    print(f'String Before reversing it: {string}')

    # Calling Function
    string = rev(string)

    print(f'String After reversing it: {string}')