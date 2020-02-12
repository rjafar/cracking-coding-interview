# 1.2 Algorithm to determine if 2 strings are permutations of each other
# Input: string s1, string s2
# Output: boolean 
# Time Complexity: O(n) where n is the length of the string

def isPermutation(s1, s2):
    if len(s1) != len(s2): return False # if string lengths are not the same they can't be permutations 

    s1sorted = ''.join(sorted(s1)) # sort both strings
    s2sorted = ''.join(sorted(s2))

    for i in range(len(s2)): # iterate through and check each character is the same
        if s1sorted[i] != s2sorted[i]: return False
    return True

res = isPermutation("abcd","bdac")
print(res)