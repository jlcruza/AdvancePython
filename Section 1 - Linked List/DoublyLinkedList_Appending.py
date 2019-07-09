class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,value):
        new = Node(value)
        new.next = self.head
        if self.head is not None:
            self.head.prev = new
        self.head = new

    def insertion(self, node, value):
        new = Node(value)
        new.next = node.next
        node.next = new
        new.prev = node
        if new.next is not None:
            new.next.prev = new

    def appending(self, value):
        new = Node(value)
        new.next = None
        if self.head is None:
            new.prev = None
            self.head = new
            return
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next  = new
        new.prev = pointer
        return

    def printing(self, node):
        while node is not None:
            print(node.data)
            node = node.next


list = LinkedList()
list.add(2)
list.add(5)
list.add(7)
list.add(9)
list.add(8)
list.insertion(list.head.next, 12)
list.appending(20)
list.printing(list.head)