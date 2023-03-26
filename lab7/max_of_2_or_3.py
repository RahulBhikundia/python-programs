def nmax(a,b,c=0):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

if __name__ == "__main__":
    a,b,c = map(int,input("Enter Three Numbers:").split())
    print(f'Maximum  of {a}, {b}, {c} is {nmax(a,b,c)}')