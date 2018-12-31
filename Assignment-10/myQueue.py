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
		if self.mCount == 0:
			self.mFirst = node
			self.mLast = node
		else:
			self.mLast.mNext = node
			self.mLast = node
		self.mCount += 1
	def dequeue(self):
		if self.mCount <= 1:
			temp_front = self.mFirst
			self.mFront = None
			self.mCount -= 1
		else:
			temp_front = self.mFirst
			self.mFirst = self.mFirst.mNext
			self.mCount -= 1
		return temp_front.mItem

	def empty(self):
		if self.mCount == 0:
			return True
		else:
			return False
	def getSize(self):
		return count
