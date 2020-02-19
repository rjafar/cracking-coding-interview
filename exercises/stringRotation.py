# 1.9 Algorithm that checks if one string is the rotation of the other. Given isSubstring(s1,s2) 
# which can only be called once
# Input: Strings s1 and s2
# Output: boolean
# Time Complexity: O(N) 

def isRotation(s1,s2):
    if len(s1) == len(s2) & len(s1) > 0: # check the strings are same length and non-empty
        s1s1 = s1 + s1 # concatenate s1 with itself
        return isSubstring(s1s1, s2) # s2 is always a substring of s1s1 so just call the method
    else:
        return False

def isSubstring(s1,s2): # helper method
    return s2 in s1

result = isRotation("waterbottle", "erbottlewat")
print(result)