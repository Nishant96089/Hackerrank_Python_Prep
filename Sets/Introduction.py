# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# Task
# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Sample Input

# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
# Sample Output

# 169.375

def average(array):
   arrL = len(set(array))
   arrSum = sum(set(array))
   result = arrSum/arrL
   return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)