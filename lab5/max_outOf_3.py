# 1. Write a Python function to find the Max of three numbers.

def max3(a,b,c):
    """function to find the Max of three numbers."""
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

if __name__ == '__main__':
    print("Enter Three numbers:")
    a,b,c = map(int,input().split())
    result = max3(a,b,c)
    print(f'{result} is the maximum')