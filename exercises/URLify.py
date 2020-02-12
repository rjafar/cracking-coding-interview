# 1.3 Algorithm to replace all spaces in string with '%20'
# Input: string s, size of s
# Output: string s with new characters
# Time Complexity: O(n) where n is the length of the string

def urlify(s, n):
    arr = list(s) # need to turn into array since strings are immutable
    j = len(arr) - 1 # gets size including extra spaces at end

    for i in range(n-1, -1, -1):  # starting from end of s, end at 0, step backwards
        if arr[i] != ' ': # if character found, move to end of array where there's extra space
            arr[j] = arr[i]
            j -= 1
        else: # if space found, add in %20 and move j to the left 3 spaces
            arr[j] = '0'
            arr[j-1] = '2'
            arr[j-2] = '%'
            j -= 3
    s = ''.join(arr) # remember to turn back into string 
    return s

    
url = urlify("Hi you  ", 6)
print(url)