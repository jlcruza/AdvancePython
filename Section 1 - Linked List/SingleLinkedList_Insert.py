class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printing(self):
		printvalue = self.head
		while printvalue is not None:
			print(printvalue.data)
			printvalue = printvalue.next

	def beg(self, data4):
		new = Node(data4)
		new.next = self.head
		self.head = new

	def end(self, data5):
		newest = Node(data5)
		if self.head is None:
			self.head = newest
			return
		lastNode = self.head
		while(lastNode.next):
			lastNode = lastNode.next
		lastNode.next = newest

	def between(self, node, datapart):
		newofall = Node(datapart)
		newofall.next = node.next
		node.next = newofall


x = LinkedList()
x.head = Node("Person 1")
data2 = Node("Person 2")
data3 = Node("Person 3")

x.head.next = data2
data2.next = data3

x.printing()
x.beg("Person 0")
x.printing()
x.end("Person 4")
x.printing()
x.between(x.head.next, "Hello")
x.printing()
