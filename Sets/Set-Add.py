# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. 
# You pick the stamps one by one from a stack of N country stamps.

# Find the total number of distinct country stamps.

# Sample Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Sample Output
# 5

n = int(input())
result = set()

for _ in range(n):
    stamp = input()
    result.add(stamp)
    
print(len(result))   