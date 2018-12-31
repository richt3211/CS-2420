class Node:

	def __init__(self, item, nxt):
		self.mItem = item
		self.mNext = nxt
class Queue:

	def __init__(self):

		self.mFirst = None
		self.mLast = None
		self.mCount = 0

	def enqueue(self, item):
		node = Node(item, None)
		if count == 0:
			self.mFirst = node
			self.mLast = node
			self.mCount += 1
		else:
			self.mLast.mNext = node
	def dequeue(self):
		if self.mFirst is None:
			return False
		temp_front = self.mFirst
		self.mFirst = self.mFirst.mNext
		count -= 1
		return temp_front.self.mItem

	def isEmpty(self):
		if self.mFirst is None:
			return False
	def getSize(self):
		return count
		