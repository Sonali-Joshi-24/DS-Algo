class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None

# time: O(1)

    def insert(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


# time: O(1)
    def insert_begin(self,data):
        newNode = Node(data)
        # base case
        if self.head == None:
            print(newNode.data)
        else:
            newNode.next = self.head
            self.head = newNode

# time: O(1)  
    def insert_After(self,node,data):    #insert in middle
        newNode = Node(data)

        # base case
        if node is None:
            return 
        else:
            newNode.next = node.next
            node.next = newNode

# Time :O(1)
    def insert_end(self,data):
        newNode = Node(data)
        # base case
        if self.head == None:
            print(newNode.data)
        else:
            self.tail.next = newNode
            self.tail = newNode 


# Time: O(N)
    def delete(self,position):
        # base case
        if self.head == None:
            return
       
        temp = self.head
        # remove the head
        if position == 0:
            self.head = temp.next
            temp = None
            return 

        # find the previous node to be deleted
        for _ in range(position-1):
            temp = temp.next
            if temp is None:
                break
        # if position is grester then no of nodes
        if temp is None:
            return
        if temp.next is  None:
            return 
        
        # temp.next is the node to be deleted
        # store the pointer to the next of node to be deleted
        n = temp.next.next
        # unlink the node
        temp.next = None
        temp.next = n    

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

# Time: O(N)
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end="==>")
            temp = temp.next
        print("Null")

# Time: O(N)
    def search(self,data):
        temp = self.head
        while temp != None:
            if data == temp.data:
                print(f'element found {data}')
                break
            else:
                temp = temp.next


l = Linklist()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.insert(40)
# ll.insert(50)


v = Linklist()
# ll2.insert(5)
# ll2.insert(15)
# ll2.insert(25)
# ll2.insert(35)


r = Linklist()

# ll.insert_end(60)
# ll.insert_begin(5)
# ll.insert_After(ll.head.next.next, 25)

# ll.delete(0)   # delete head
# ll.delete(3)   # delete end

# ll.display()
# ll.search(30)

