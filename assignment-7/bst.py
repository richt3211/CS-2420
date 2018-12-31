class Node:

	def __init__(self, item):
		self.mItem = item
		self.mLeft = None
		self.mRight = None
class UUC:

	def __init__(self):
		self.mRoot = None # initializing root of tree to None
		self.mSize = 0
	def insert(self, item):
		if self.exists(item): # checking to see if the item already exists before I insert into the tree
			return False
		self.mRoot = self.insertR(item, self.mRoot) #calling insert recursively using root as current
		return True
	def insertR(self, item, current): # insert recursive
		if current is None:  # if current is none, meaning that it doesn't have an assignment. 
		# this makes it so that the very first item will be inserted(self.mRoot is None)
		# and also that nodes lef and right pointers that are filled will be down the 
		#tree
			n = Node(item)
			current = n
			self.mSize +=1
		elif item < current.mItem:
			current.mLeft = self.insertR(item, current.mLeft)
		else:
			current.mRight = self.insertR(item, current.mRight)
		return current
	def delete(self, dummy):
		if not self.exists(dummy):
			return False
		self.mRoot = self.deleteR(dummy, self.mRoot)
		return True
	def deleteR(self, dummy, current):
		if dummy < current.mItem: # if the item is less
			current.mLeft = self.deleteR(dummy, current.mLeft) # recurse down the left side
		elif dummy > current.mItem:# if the item is more
			current.mRight = self.deleteR(dummy, current.mRight) # recurse down the right side
		else: # if we are at the time that we need to delete
			if current.mLeft is None and current.mRight is None: #if the node has no children
				current = None
			elif current.mLeft is None: # one left child
				current = current.mRight
			elif current.mRight is None: # one right child
				current = current.mLeft
			else: #two children
				s = current.mRight # s is in order succesor
				while not s.mLeft is None:
					s = s.mLeft
				current.mItem = s.mItem # copy the in order succesor to item to delte
				current.mRight = self.deleteR(s.mItem, current.mRight) # delete the in order succesor
		return current
	def exists(self, item):
		return self.existsR(item, self.mRoot)
	def existsR(self, dummy, current):
		if current is None:
			return False
		if dummy < current.mItem:
			return self.existsR(dummy, current.mLeft)
		elif dummy > current.mItem:
			return self.existsR(dummy, current.mRight)
		elif dummy == current.mItem:
			return True
	def retrieve(self, item):
		return self.retrieveR(item, self.mRoot)
	def retrieveR(self, item, current):
		if current is None:
			return None
		if current.mItem == item:
			return current.mItem
		elif item > current.mItem:
			return self.retrieveR(item, current.mRight)
		elif item < current.mItem:
			return self.retrieveR(item, current.mLeft)
	def traverse(self, callback):
		self.traverseR(self.mRoot, callback)
	def traverseR(self, current, callback):
		if current:
			callback(current.mItem)
			self.traverseR(current.mLeft, callback)
			self.traverseR(current.mRight, callback)
		return
	def getSize(self):
		return self.mSize
