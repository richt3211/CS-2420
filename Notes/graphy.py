class Graph:

	def __init__(self, numVariables):
		self.mNeighbors = []
		for x in range(numVariables):
			self.mNeighbors.append([])
	def addEdge(v0,v1):
		self.mNeighors[v0].append(v1)
	def breadthFirstSearch(v0,v1):

	def depthFirstSearch(v0,v1):

	def getNeighbors(v0,v1):
		return self.mNeighbors[v0]
	def isEdge(v0,v1):
		for x in self.mNeighbors[v0]:
			if x == v1:
				return True
			else:
				return False

