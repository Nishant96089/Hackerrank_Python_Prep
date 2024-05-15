# You have a non-empty set s, and you have to execute N commands given in N lines.

# The commands will be pop, remove and discard.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# Sample Output
# 4

# Read input
n = int(input())
s = set(map(int, input().split()))
N = int(input())

# Processing Commands
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    if cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    if cmd[0] == 'discard':
        s.discard(int(cmd[1]))
        
print(sum(s))