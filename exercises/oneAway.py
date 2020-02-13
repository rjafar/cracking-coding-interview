# 1.5 Algorithm to check whether from two given strings if they are one (or zero) edits away where
# edits are: add, remove, or replace a character
# Input: string s1, string s2
# Output: boolean
# Time Complexity: O(n) where n is the length of the shorter string

def isOneAway(s1, s2): 
    arr1 = list(s1)
    arr2 = list(s2)

    if len(s1) == len(s2): # if length is same, check for more than one replaced char
        found = False
        for i in range(len(s1)):
            if arr1[i] != arr2[i]: # different char found
                if found == True: # if this is the 2nd difference, return False
                    return False
                found = True
        return True # only found one edit, return True
    
    elif ((len(s1)-1) == len(s2)) | ((len(s1)+1) == len(s2)): # if size of strings is off by one
        arr1 = arr1 if len(s1) < len(s2) else arr2 # find shorter of strings
        arr2 = arr2 if len(s1) < len(s2) else arr1

        i = 0 # index tracker for s1
        j = 0 # index tracker for s2
        while i < len(s1) & j < len(s2):
            if arr1[i] != arr2[j]: # if difference found
                if i != j: # if index is different, more than one edit
                    j = j + 1 # move j along
                    return False
            else:
                i = 1 + 1 # move both indexes along since strings match so far
                j = j + 1
        return True
    else:
        return False

result = isOneAway("pale", "ale")
print(result)
result = isOneAway("pales", "ale")
print(result)