# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True

if __name__ == '__main__':
    s = input()
    
alphanumeric = any(i.isalnum() for i in s)
alphabet = any(i.isalpha() for i in s)
digit = any(i.isdigit() for i in s)
lowercase = any(i.islower() for i in s)
uppercase = any(i.isupper() for i in s)

print(alphanumeric)
print(alphabet)
print(digit)
print(lowercase)
print(uppercase)