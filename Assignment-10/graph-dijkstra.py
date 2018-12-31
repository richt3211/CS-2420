import sys
import heap
class Graph:

	def __init__(self, numVariables):
		self.mNumVariables = int(numVariables)
		self.mNeighbors = [list() for x in range(self.mNumVariables)]
	def addEdge(self,v0,v1, cost):
		self.mNeighbors[v0].append((v1, cost))
	def dijkstrasSearch(self, v0, v1):
		previous = [-1] * self.mNumVariables # setting previous list
		cost = [-1] * self.mNumVariables # setting cost list
		q = heap.priorityQueue() # initializing heap
		first_node = (v0,0) # making the first node in the heap the start of the search, with priority 0
		q.enqueue(first_node) # enqueueing the first node
		previous[v0] = v0 # setting the first's previous to itself
		cost[v0] = 0 # setting the cost to 0
		path = [] # initializing path variable.
		while q.isEmpty() == False:
			# while the queue is not empty, and we have a path
			current = q.dequeue() # get the top of the queue in current
			# if current is destination that we want, we want to reconstruct the path and return it, and brake the loop
			if current[0] == v1: # if the value of the current is what we're looking for, reconstruct path
				current_path = v1 # the current path variable for tracking
				next_path = v1 # the next path variable for tracking
				count = 0 # keeping track of where we are in list
				path.append(current_path) # starting the path out with the end
				next_path = previous[path[count]] # setting the next path to be the value of the index of the current path variable
				# while 
				while current_path != next_path:
					 # if we have a repeat in our path, that's when we stop
					path.append(next_path) # appending the next path variable
					current_path = next_path # setting the current to the next for next iteration
					next_path = previous[path[count + 1]] # setting the next variable the next one in the list
					count += 1 # increasing the count
				path.reverse()
				return path
			neighbors = self.getNeighbors(current[0])
			for x in neighbors:
				if previous[x[0]] == -1:
					previous[x[0]] = current[0]
					cost[x[0]] = x[1] + cost[current[0]]
					node = x[0], cost[x[0]]
					q.enqueue(node)
			for x in neighbors:
				if previous[x[0]] != -1 and (cost[current[0]] + x[1]) < cost[x[0]]:
					previous[x[0]] = current[0]
					node = q.dequeue()
					node = (node[0], cost[current[0]] + x[1])
					cost[x[0]] = node[1]
					q.enqueue(node)
		return None
	def getNeighbors(self,v):
		return self.mNeighbors[v]
	def getEdges(self):
		return self.mNeighbors
	def isEdge(self,v0,v1):
		for x in self.mNeighbors[v0]:
			if x[0] == v1:
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
				graph.addEdge(int(data[0]), int(data[1]), int(data[2]))
				count += 1
				continue
			if count == (2 + numEdges):
				numTest = int(line.strip())
				count +=1
				continue
			if count > (2 + numEdges):
				test = line.split()

				path = graph.dijkstrasSearch(int(test[0]), int(test[1]))
				# path = graph.breadthFirstSearch(int(test[0]), int(test[1]))
				print(path)
				count +=1
				continue

if __name__ == "__main__":
	main()