import sys
import stack
import myQueue
class Graph:

	def __init__(self, numVariables):
		self.mNumVariables = int(numVariables)
		self.mNeighbors = [list() for x in range(self.mNumVariables)]
	def addEdge(self,v0,v1):
		self.mNeighbors[v0].append(v1)
	def depthFirstSearch(self,v0,v1):
		visited = []
		stack1 = stack.Stack()
		stack1.push(v0)
		visited.append(v0)
		while stack1.top() != v1:
			if stack1.empty() == True:
				return None
			neighbors = self.getNeighbors(stack1.top())
			possible_visit = []
			can_visit = False
			for x in neighbors:
				if x not in visited:
					possible_visit.append(x)
					can_visit = True
			if can_visit == False:
				stack1.pop()
				continue
			else:
				next_visit = min(possible_visit)
				stack1.push(next_visit)
				visited.append(next_visit)
		path = []
		while stack1.empty() == False:
			path.append(stack1.pop())
		path.reverse()
		return path
	def breadthFirstSearch(self, v0,v1):
		previous = [-1] * self.mNumVariables
		q = myQueue.Queue()
		q.enqueue(v0)
		previous[v0] = v0
		path = []
		while q.empty() == False:
			current = q.dequeue()
			# if current is destination that we want, we want to reconstruct the path and return it, and brake the loop
			if current == v1:
				current_path = v1
				next_path = v1
				count = 0
				path.append(current_path)
				next_path = previous[path[count]]
				while current_path != next_path:
					path.append(next_path)
					current_path = next_path
					next_path = previous[path[count + 1]]
					count += 1
				path.reverse()
				return path
			neighbors = self.getNeighbors(current)
			neighbors.sort()
			for x in neighbors:
				if previous[x] == -1:
					q.enqueue(x)
					previous[x] = current
		return None
	def getNeighbors(self,v):
		return self.mNeighbors[v]
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
				count += 1
				continue
			if count == (2 + numEdges):
				numTest = int(line.strip())
				count +=1
				continue
			if count > (2 + numEdges):
				test = line.split()
				print("Running breadthFirst Search")
				path = graph.breadthFirstSearch(int(test[0]), int(test[1]))
				print(path)
				print("Running depthFirst Search")
				path = graph.depthFirstSearch(int(test[0]), int(test[1]))
				print(path)
				count +=1
				continue

if __name__ == "__main__":
	main()