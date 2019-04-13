class Stack(object):

	def __init__(self):
		self.stack = []

	def add(self, dataValue):
# use list append method to add element
		if dataValue not in self.stack:
			self.stack.append(dataValue)
			return True
		else:
			return False

	def remove(self):
		if len(self.stack) <= 0:
			return ("No element in the stack")
		else:
			return self.stack.pop()

# use peek to look at the top of the stack
	def peek(self):
		return self.stack[0]

Astack = Stack()
Astack.add("Mon")
Astack.add("Tue")
print(Astack.peek())
print(Astack.remove())
Astack.add("Wed")
Astack.add("Thu")
print(Astack.peek())
print(Astack.remove())
