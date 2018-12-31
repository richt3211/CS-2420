# a priorityQueue using a heap as it's implentation


class priorityQueue():


	def __init__(self):
		self.mItems = []
		self.mLength = 0

	def enqueue(self, node):
		if len(self.mItems) == 0:
			self.mItems.append(node)
			self.mLength += 1
		else:
			self.mItems.append(node)
			child = len(self.mItems) -1
			parent = (child-1)//2
			while self.mItems[child][1] < self.mItems[parent][1]:
				self.mItems[child], self.mItems[parent] = self.mItems[parent], self.mItems[child]
			self.mLength +=1
	def dequeue(self):
		if len(self.mItems) == 0:
			return False
		if len(self.mItems) == 1:
			return self.mItems.pop()
		else:
			priority = self.mItems[0]
			self.mItems[0] = self.mItems[len(self.mItems) -1]
			self.mItems.pop()
			self.mLength -= 1
			parent = 0
			childL = parent * 2 + 1
			childR = parent * 2 + 2
			done = False
			while done == False:
				if childL == 0 and self.mItems[parent][1] > self.mItems[child][1]:
					parent = childL
					childL = parent * 2 + 1
					childR = parent * 2 + 2
				elif childR == 0 and self.mItems[parent][1] > self.mItems[childR][1]:
					parent = childR
					childL = parent * 2 + 1
					childR = parent * 2 + 1
				else:
					done = True
			return priority
	def isEmpty(self):
		 if len(self.mItems) == 0:
		 	return True
		 else:
		 	return False
	def getSize(self):
		return self.mLength
