#  You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2

def count_substring(string, sub_string):
    stringL = len(string)
    subStringL = len(sub_string)
    count = 0
    for i in range(stringL-subStringL+1):
        if (string[i:(i + subStringL)] == sub_string):
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

