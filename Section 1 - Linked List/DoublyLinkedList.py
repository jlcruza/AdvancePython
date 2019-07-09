class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        a = Node(value)
        a.next = self.head
        if self.head is not None:
            self.head.prev = a
        self.head = a

    def printing(self, node):
        while(node is not None):
            print(node.data)
            last = node
            node = node.next


list = LinkedList()
list.add("Value")
list.printing(list.head)