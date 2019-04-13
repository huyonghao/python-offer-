class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class SLinkedList(object):
	def __init__(self):
		self.headvalue = None

	def listprint(self):
		printvalue = self.headvalue
		while printvalue is not None:
			print(printvalue.value)
			printvalue = printvalue.next

	def addbegining(self, newdata):
		newnode = Node(newdata)
		# update the new node
		newnode.next = self.headvalue
		self.headvalue = newnode

	def addending(self, newdata):
		newnode = Node(newdata)
		# no node and add node
		if self.headvalue is None:
			self.headvalue = newnode
			return
		laste = self.headvalue
		# move to the end
		while(laste.next):
			laste = laste.next
		# have node and add node
		laste.next = newnode

	def addinner(self, middle_node, newdata):
		if middle_node is None:
			print("The mentioned node is absent")
			return
		newnode = Node(newdata)
		newnode.next = middle_node.next
		middle_node.next = newnode

	def removenode(self, removekey):
		headvalue = self.headvalue
		if (headvalue is not None):
			if(headvalue.value == removekey):	
				self.headvalue = headvalue.next
				headvalue = None
				return
		while (headvalue is not None):
			if (headvalue.value == removekey):
				break
			prev = headvalue
			headvalue = headvalue.next
		if (headvalue == None):
			return
		prev.next = headvalue.next
		headvalue = None

list1 = SLinkedList()
list1.headvalue = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headvalue.next = e2
e2.next = e3
list1.addbegining("Sun")
list1.addending("Sun")
list1.addinner(list1.headvalue.next.next, "Fri")
list1.removenode("Wed")
list1.listprint()