class Queue(object):

	def __init__(self):
		self.queue = list()

	def addTop(self, dataValue):
# insert method to add element
		if dataValue not in self.queue:
			self.queue.insert(0, dataValue)
			return True
		return False

	def removeFront(self):
		if len(self.queue) > 0:
			return self.queue.pop()
		return ("No element in queue!")			

	def size(self):
		return len(self.queue)

TheQueue = Queue()
TheQueue.addTop("Mon")
TheQueue.addTop("Tue")
TheQueue.addTop("Wed")
print(TheQueue.size())
print(TheQueue.removeFront())
print(TheQueue.removeFront())
print(TheQueue.removeFront())