class Node:
    def __init__(self,data,next=None):
        self.data = data                  # data
        self.next = next                  # pointing to next node

class LinkedList:
    def __init__(self):
        self.head = None                  # headNode
    def insert(self,data):
        newNode = Node(data)              # creating a Node and assiging to newNode
        if (self.head):                   # check if the head is there
            current = self.head           # assigning to current node
            while(current.next):          # loop through till next node is None
                current = current.next 
            current.next = newNode        # newNode is added to last of the LinkedList
        else:
            self.head = newNode

    def printLL(self):                    # print all LinkedList data
        current = self.head
        # all_data = []
        while(current):                   # loop through till next node is None
            # all_data.append(current.data)
            print(current.data)
            current = current.next
        # print(all_data)
    def insert_start(self,data):          # Insert the data that your passing at the start 
        prev = self.head                  # previous data means starting data save to a variable
        self.head = Node(7)               # create a node for and setting that head variable
        current = self.head               
        current.next = prev               # refering next to previous that we have saved
    def insert_mid(self,data,mid_position): # inserting the data in particular position
        current,pos = self.head,1
        newNode = Node(data)
        while (current.next) and (pos < mid_position-1):
            current = current.next
            pos += 1
        prev = current.next
        current.next = newNode
        current.next.next = prev
    def delete_end(self):
        current = self.head
        while (current.next):
            prev = current
            current = current.next
        prev.next = None
        del current
    def delete_start(self):
        current = self.head
        self.head = current.next
        del current
    def delete_pos(self,pos):
        current,p = self.head,1
        while (current.next) and (p < pos):
            p += 1
            prev = current
            current = current.next
        prev.next = current.next
        del current
    def update(self,data,update_data):
        current,pos = self.head,1
        while (current):
            pos += 1
            if current.next != None:
                if current.next.data == data:
                    self.delete_pos(pos)
                    self.insert_mid(update_data,pos)
                    return
            else:
                print("entered number is not in the list")
            current = current.next







L1 = LinkedList()
L1.insert(3)
L1.insert(4)

L1.insert_start(7)

L1.insert(10)

L1.insert_mid(15,3)


L1.delete_end()

L1.delete_start()

L1.delete_pos(2)

L1.update(15,88)
L1.printLL()
