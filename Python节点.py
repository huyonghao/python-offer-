class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.next = None

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")

e1.next = e3
e3.next = e2
e2.next = e4

thisvalue = e1

while thisvalue:
	print(thisvalue.value)
	thisvalue = thisvalue.next
