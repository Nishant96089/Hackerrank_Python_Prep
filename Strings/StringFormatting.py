# Given an integer,n, print the following values for each integer i from 1 to n:

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

def print_formatted(number):
    width = len("{0:b}".format(number))
    
    for i in range(1,number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)