from linkedList import LinkedList     
    
# Desctiption: function that sums two numbers represented as linked lists
# Input: 2 linked lists
# Output: linked list representing a sum of the two inputs
# Time Complexity: O(n)

def sumLinkedLists(LL1,LL2):
    LL3 = LinkedList() # init result linked list
    curr1 = LL1.head # get heads of both input linked lists
    curr2 = LL2.head
    carry = 0 # carryover value
    while ((curr1 is not None) | (curr2 is not None)):
        resultSum = curr1.data + curr2.data # add data
        LL3.insert((resultSum % 10) + carry) # get one's place digit then add carry
        carry = 1 if resultSum >= 10 else 0 # determing carry
        curr1 = curr1.next # move pointers along
        curr2 = curr2.next
    return LL3

# driver code and test
LL = LinkedList()
LL.insert(7)
LL.insert(1)
LL.insert(6)
LL2 = LinkedList()
LL2.insert(5)
LL2.insert(9)
LL2.insert(2)
LL3 = LinkedList()
LL3.insert(2)
LL3.insert(1)
LL3.insert(9)
result = sumLinkedLists(LL,LL2)
print("Result should be = ")
LL3.printLinkedList()
print("Resulting sum = ")
result.printLinkedList()