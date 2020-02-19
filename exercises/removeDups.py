# 2.1 Algorithm that removes duplicates from an unsorted linked list
# Input: linked list
# Output: linked list without duplicates
# Time Complexity: O(N)

def removeDups(ll):
    m = {} # map that holds each unique character
    count = 0 # counts duplicates
    for i in range(len(ll)): # iterate linked list
        if count > 0: # if duplicates found, update iterator i
            i -= count
        if ll[i] not in m: # if new character, add to map
            m[ll[i]] = 1
        else: # if duplicate character, remove it and update duplicate count
            ll.pop(i)
            count += 1
    return ll

ll = [1,2,1,3,1,2]
print(removeDups(ll))