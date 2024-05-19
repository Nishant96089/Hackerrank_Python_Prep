# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import random
import string

msg = input("Enter message: ")
words = msg.split(" ")
cmd = int(input("Enter 1 for Coding or 0 for Decoding : "))
cmd = True if (cmd == 1) else False
nWords = []

if(cmd):
    for word in words:
        if(len(word) >= 3):
            r1 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            r2 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            newStr = r1 + word[1:] + word[0] + r2
            nWords.append(newStr)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))
else:
    for word in words:
        if(len(word) >= 3):
            newStr = word[3:-3]
            newStr = newStr[-1] + newStr[:-1]
            nWords.append(newStr)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))