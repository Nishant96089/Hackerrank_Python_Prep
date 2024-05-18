# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format

# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

def is_subset(A, B):
    return A.issubset(B)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n_A = int(data[index])
        index += 1
        A = set(map(int, data[index:index + n_A]))
        index += n_A
        n_B = int(data[index])
        index += 1
        B = set(map(int, data[index:index + n_B]))
        index += n_B
        
        results.append(is_subset(A, B))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
