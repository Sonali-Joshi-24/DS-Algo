# time: O(n) space: O(1)

from Linklist import l 

a = [1,2,3,4,5,6,7,8]
[l.insert(i) for i in a]


def DetectLoop(l):
    fast = l.getHead()
    slow = l.getHead()
    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return "loop exist"
    print('loop does not exist')



l.head.next.next.next.next = l.head.next    # code for loop exist
print(DetectLoop(l))
