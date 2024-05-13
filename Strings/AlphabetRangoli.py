# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Sample Input
# 5
# Sample Output

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    # Create the upper part of the rangoli
    for i in range(size-1, 0, -1):
        row = ['-'] * (2*size-1)
        for j in range(size-i):
            row[size-1-j] = row[size-1+j] = alphabet[j+i]
        print('-'.join(row))

    # Create the center line of the rangoli
    for i in range(0, size):
        row = ['-'] * (2*size-1)
        for j in range(0, size-i):
            row[size-1-j] = row[size-1+j] = alphabet[j+i]
        print('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)