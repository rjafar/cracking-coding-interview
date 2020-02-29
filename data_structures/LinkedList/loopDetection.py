from linkedList import LinkedList

# Description: Find node where circular linked lists begins
# Input: linked list
# Output: beginning of loop Node
# Time Complexity: O(n)

def loopDetection(LL):
    curr = LL.head
    m = {}

    while(curr):
        if curr not in m:
            m[curr] = 1
        else:
            return curr
        if curr.next:
            curr = curr.next