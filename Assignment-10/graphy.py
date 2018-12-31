import sys
class Graph:

	def __init__(self, numVariables):
		numVariables = int(numVariables)
		self.mNeighbors = [list() for x in range(numVariables)]
	def addEdge(self,v0,v1):
		self.mNeighbors[v0].append(v1)
	# def breadthFirstSearch(v0,v1):

	# def depthFirstSearch(v0,v1):

	def getNeighbors(self,v0,v1):
		return self.mNeighbors[v0]
	def getEdges(self):
		return self.mNeighbors
	def isEdge(self,v0,v1):
		for x in self.mNeighbors[v0]:
			if x == v1:
				return True
			else:
				return False

def main():
	with open(sys.argv[1], 'r') as file:
		count = 0
		numEdges = 0
		for line in file:
			if count == 0:
				numVertices = int(line.strip())
				graph = Graph(numVertices)
				count += 1
				continue
			if count == 1:
				numEdges = int(line.strip())
				count += 1
				continue
			if count >= 2 and count < (2 + numEdges):
				data = line.split()
				graph.addEdge(int(data[0]), int(data[1]))
				print("adding edge")
				count += 1
		edge = graph.isEdge(1,3)
		print (edge)
		print (graph.getEdges())


if __name__ == "__main__":
	main()