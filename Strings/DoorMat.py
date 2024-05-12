# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N*M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Sample Input
# 9 27

# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------


row,column = map(int,input().split(' '))

for i in range(1,row,2):
    print((".|."*i).center(column,'-'))

print("WELCOME".center(column,'-')) 

for i in range(row-2,-1,-2):
    print((".|."*i).center(column,'-'))