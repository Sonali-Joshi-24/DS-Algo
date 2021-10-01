class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class DoublyLinklist:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        newNode = Node(data)

        # check if head is none
        if self.head == None:
            self.head = newNode
            self.tail = newNode

            self.head.prevNode = None
            self.tail.nextNode = None
        
        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail

            self.tail = newNode
            self.tail.nextNode = None

    def insert_at_begining(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

            self.head.prevNode = None
            self.tail.nextNode = None

        else:
            self.head.prevNode = newNode
            newNode.nextNode = self.head

            self.head = newNode
            self.head.prevNode = None

    def insert_at_end(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

            self.head.prevNode = None
            self.tail.nextNode = None

        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail

            self.tail = newNode
            self.tail.nextNode = None

    def insert_in_between(self,data,position):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

            self.head.prevNode = None
            self.tail.nextNode = None

        curr = self.head
        for _ in range(position - 1):
            curr = curr.nextNode
        temp = curr.nextNode
        temp.prevNode = curr

        curr.nextNode = newNode
        newNode.prevNode = curr
        newNode.nextNode = temp
        temp.prevNode = newNode

        # 1 2 3  4  5
        #     c  t


    def delete_from_begining(self):
        if self.head == None:
            return
        else:
            if self.head != self.tail:
                self.head = self.head.nextNode
                self.head.prevNode = None
            else:
                self.head = self.tail = None

    def delete_from_end(self):
        if self.head == None:
            return
        else:
            if self.head != self.tail:
                self.tail = self.tail.prevNode
                self.tail.nextNode = None
            else:
                self.head = self.tail = None

    def delete_from_position(self,position):# here temp is node to be deleted
        if self.head == None:
            return

        curr = self.head
        for _ in range(position - 1):
            curr = curr.nextNode

        temp = curr.nextNode
        temp.prevNode = curr

        curr.nextNode = temp.nextNode
        temp.nextNode.prevNode = curr

        # 1 2 3  4  5
        #     c  t   





    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <==> ")
            temp = temp.nextNode
        print("Null")

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail



d = DoublyLinklist()

a = [1,2,3,4,5]
[d.insert(i) for i in a]
# d.insert_at_begining(7)
# d.insert_at_end(6)
# d.insert_in_between(8,3)
# d.delete_from_begining()
# d.delete_from_end()
d.delete_from_position(3)
d.display()




