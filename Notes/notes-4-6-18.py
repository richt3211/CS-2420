class Graph:

	def __init__(self, numVariables):
		#specify the entire graph using the addEdge function
		self.mNeighors = [
							0[1]
							1[3]
							2[3]
							3[2,0]
							] # this is the way that the list is going to tlook to keep track of the vertices and their edges
							
	def addEdge(v0, v1):

	def findPathBreadthFirst(v0, v1):
		# this is going to find the quickest path from one point to the other using a breadth first approach
	def findPathDepthFirst(v0, v1):
		# this is going to ifnd the quickest path from one point to the other using a depth first approach
	def getNeighors(v): 
		#given a vertex, what are the neighbors
		# return list with numbers of where you can go
	def isEdge(v0, v1): 
		#is there an edge between these two points, only works if the edge is pointed in the right direction


#depth first uses a stack in it's algorithmn
# depth ifrst uses a list of visited vertices
# breadth first uses a queue in it's algorithmn
# breadth first also uses a list of visised vertices, but it also relies on a list that is previously visited. 

prev = [
		0, -1
		1, -1
		2, -1
		3, -1
		4, -1]

def breadthFirstSearch(v0,v1):
	#q = myQueue()
	prev = [-1] * self.numVertices
	# put v0 in q, and set it's prev
	while q is not empty:
			c = q.dequeue()
			if c == v1:
				build path and return it
	for all unvisited neighbors of c,
		set prev to c, put in q