# 1.1 Algorithm to determine if string has all unique characters
# Input: string s
# Output: boolean 
# Time Complexity: O(n)

def isUnique(s):
    map = {}
    for c in s: # iterate each character in s
        if c in map: # if we've seen it before, not unique
            return False
        else: # put in map
            map[c] = c
    return True # all unique

result = isUnique("howdy")
print(result)
