# 1.6 Algorithm to compress a string by counting how many of each char there is. E.g. aabccca = a2b1c3a1
# Input: string s
# Output: compressed string or original string if it's shorter
# Time Complexity: O(n) where n is the length of the string'

def compress(s):
    compressedStr = s[0] # grab first character to place in our new string
    count = 1

    for i in range(len(s)-1): # stop before the last to avoid going out of bounds
        if s[i] == s[i+1]: # two consecutive letters
            count += 1 # increment counter
        else: # found a different character
            compressedStr += str(count) # append total count of last character sequence
            compressedStr += s[i+1] # append new character
            count = 1 # reset counter
    if count >= 1: # handle last character
        compressedStr += str(count)
    
    compressedStr = compressedStr if len(compressedStr) < len(s) else s # check which string is shorter

    return compressedStr

result = compress("abcd")
print(result)