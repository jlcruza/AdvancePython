class Node:
	def __init__(self, datavalue=None):
		self.datavalue = datavalue
		self.nextvalue = None


class LinkedList:
	def __init__(self):
		self.headvalue = None

	def printing(self):
		printvalue = self.headvalue
		while printvalue is not None:
			print(printvalue.datavalue)
			printvalue = printvalue.nextvalue

x = LinkedList()
x.headvalue = Node("Person 1")
data2 = Node("Person 2")
data3 = Node("Person 3")

x.headvalue.nextvalue = data2
data2.nextvalue = data3

x.printing()
