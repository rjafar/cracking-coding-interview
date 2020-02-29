from linkedList import LinkedList

# Description: Check if a linked list is a palindrome
# Input: linked list
# Output: Boolean
# Time Complexity: O(n)

def isLLPalindrome(LL):
    stack = []
    curr = LL.head # get head
    while (curr):
        stack.append(curr.data) # append all data to stack
        curr = curr.next # move along
    if stack[::-1] == stack: # check if reversed stack list is the same as original 
        return True
    else:
        return False

LL = LinkedList()
LL.insert('m')
LL.insert('o')
LL.insert('m')
print(isLLPalindrome(LL))

