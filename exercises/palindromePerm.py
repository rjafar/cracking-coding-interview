# 1.4 Algorithm to check whether a given string is a permutation of a palindrome
# Input: string s
# Output: boolean
# Time Complexity: O(n) where n is the length of the string

def isPalindromePerm(s):
    s = s.replace(' ', '') # get rid of all spaces
    arr = list(s)
    map = {}

    for letter in arr: # iterate string
        if letter not in map: # if letter not seen before, add to map with count value of 1
            map[letter] = 1
        else: # increment current  count of letter
            map[letter] += 1
    
    foundOdd = False # tracks if we find an odd count
    for val in map.values(): # iterate through map counts
        if val % 2 == 1:
            if foundOdd == True: # found 2nd odd count, return False
                return False
            foundOdd = True # found 1 odd count
    return True # all even counts or only 1 odd count, return True


result = isPalindromePerm('tact coa')
print(result)

