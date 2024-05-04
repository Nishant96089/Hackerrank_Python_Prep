# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. 
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    max_Val = max(arr)
    val_Count = arr.count(max_Val)
    
    for i in range(val_Count):
        arr.remove(max_Val)
    print(max(arr))