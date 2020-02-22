from linkedList import LinkedList

# Description: Check where 2 linked lists intersect
# Input: linked lists LL1, LL2
# Output: intersecting Node or None
# Time Complexity: O(n)

def intersection(LL1, LL2):
    curr1 = LL1.head
    curr2 = LL2.head
    m = {}

    while ((curr1 is not None) | (curr2 is not None)):
        if curr1 not in m: # if not in map, insert
            m[curr1] = 1
        else: # it is in map so it's an intersection
            return curr1
        if curr2 not in m:
            m[curr2] = 1
        else:
            return curr2

        if curr1.next:
            curr1 = curr1.next
        if curr2.next:
            curr2 = curr2.next
    return None # no intersections