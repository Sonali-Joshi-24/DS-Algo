'time: O(N) and Space: O(1)'
from Linklist import l 

a = [1,2,3,4,5]
[l.insert(i) for i in a]


def findMiddle(l):
    fast_ptr = l.getHead()
    slow_ptr = l.getHead()

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.data
print(findMiddle(l))