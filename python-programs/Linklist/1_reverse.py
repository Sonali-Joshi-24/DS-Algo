# Time : O(N)      Space: O(1)


from Linklist import ll 

def reverse_ll(self):
    current = self.head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev

reverse_ll(ll)
print('reverse linklist is',end =' ')
ll.display()