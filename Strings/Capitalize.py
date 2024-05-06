#!/bin/python3

# import math
# import os
# import random
# import re
# import sysc

def solve(s):
    names = s.split(' ')
    capitalized_names = [name.capitalize() for name in names]
    return ' '.join(capitalized_names)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()