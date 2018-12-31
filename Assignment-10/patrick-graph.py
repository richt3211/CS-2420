"""
Write a program that loads a graph from an input file.
The first line contains the number of vertices.
The second line contains the number of edges.
The next several lines contain pairs of vertex indices, one for each edge,
indicated there is a directed edge from the first vertex to the second.
The next line contains the number of test cases.
The next several lines contains pairs of vertex indices, one for each edge,
asking for a path from the first to the second, or 'None.'

After loading the graph information,
use a depth first search to find a path (or 'None') for all of the test cases.
Repeat using a breadth first search.
"""


import pygame
import math
import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class Stack:

    def __init__(self):
        self.mStack = []
        self.mLength = 0
        return
    def top(self):
        if self.empty() == False:
            return self.mStack[self.mLength-1]
    def push(self, item):
        self.mStack.append(item)
        self.mLength +=1
        return
    
    def pop(self):
        if self.empty() == False:
            a = self.mStack.pop(self.mLength-1)
            self.mLength-=1
        return a
    
    def empty(self):
        if self.mLength <= 0:
            return True
        else:
            return False
        
    def size(self):
        return self.mLength
    
class Vertex:
    def __init__(self, index, x, y):
        self.mIndex = index
        self.mX = x
        self.mY = y
        return
    def getIndex(self):
        return self.mIndex
    def getX(self):
        return self.mX
    def getY(self):
        return self.mY

    def draw( self, surface ):
        pygame.font.init()
        pos = ( int ( self.mX ), int ( self.mY ) )
        pygame.draw.circle( surface, (0, 0, 255), pos, 8, 0 )
        myFont = pygame.font.SysFont("arial", 12)
        text = myFont.render(str(self.mIndex), True, (255,255,255))
        surface.blit(text, (self.mX-5, self.mY-7))
        return

class Graph:
    
    def __init__(self, numVertices, surface, width, height):
        self.mNeighbors = []
        self.mWidth = width
        self.mHeight = height
        for i in range(numVertices+1):
            self.mNeighbors.append([])

    #adds edge between to points
    def addEdge(self, v0, v1):
        self.mNeighbors[v0].append(v1)
        return

    #returns nearbors around a vertex
    def getNeighbor(self, v0):
        return self.mNeighbors[v0]

    def isEdge(self, v0, v1):
        for i in self.mNeighbors[v0]:
            if i == v1:
                return True
        return False

    def getNeighborNum(self, v0):
        return len(self.mNeighbors[v0])

    def getNeighbors(self):
        return self.mNeighbors

    def draw(self, s, solution):
        vList = []
        pygame.Surface.fill(s, (255,255,255))
        l = len(self.mNeighbors)
        w = math.sqrt(l)
        #size is the square root rounded up
        size = l // w + 1
        xScale = self.mWidth // size 
        yScale = self.mHeight // size
        translate = xScale//2
        x = -translate
        y = yScale//2
        #Get the x,y for each vertex
        for i in range(l):
            stagger = random.randint(-25,25)
            if x >= xScale*size-xScale:
                x = translate
                y += yScale
            else:
                x += xScale
            v = Vertex(i, x+stagger, y+stagger)
            vList.append(v)
        #Print edges
        for i in range(l):
            for j in self.mNeighbors[i]:
                if j:
                    pygame.draw.line( s, (0, 255,0), (vList[i].getX(), vList[i].getY()), (vList[j].getX(),vList[j].getY()), 2)
        #Print Vertices
        for v in vList:
            v.draw(s)
        #Print Solution
        if solution != False:
            for i in range(len(solution)):
                if i < len(solution)-1:
                    pygame.draw.line( s, (255, 0,0), (vList[solution[i]].getX(), vList[solution[i]].getY()), (vList[solution[i+1]].getX(),vList[solution[i+1]].getY()), 2)
        return

    def findPathBreadth(self, v0, v1):
        q = Queue()
        prev = []
        for i in range(len(self.mNeighbors)):
            prev.append(-1)
        q.enqueue(v0)
        prev[v0] = v0

        while q.isEmpty() == False:
            current = q.dequeue()
            if current == v1:
                c = current
                path = []
                while c != v0:
                    path.append(c)
                    c = prev[c]
                path.append(v0)
                path.reverse()
                print(path)
                return path

            for n in self.mNeighbors[current]:
                if prev[n] == -1:
                    q.enqueue(n)
                    prev[n] = current
        return False


    def findPathDepth(self, v0, v1):
        s = Stack()
        visited = []
        for i in range(len(self.mNeighbors)):
            visited.append(False)

        s.push(v0)
        visited[v0] = True

        while not s.empty():
            current = s.top()
            if current == v1:
                #build path and return it
                path = []
                for x in range(s.size()):
                    path.append(s.pop())
                path.reverse()
                print(path)
                return path
            
            unvisited = -1
            for n in self.mNeighbors[current]:
                if visited[n] == False:
                    unvisited = n
                    s.push(unvisited)
                    visited[unvisited] = True
                    break
            if unvisited == -1:
                s.pop()
        return False
    
############END CLASSES##############
    
def randomGraph(numV, win, width, height, complexity):
    r = Graph(numV, win, width, height)
    # 0 1 2 3 4
    for v in range(len(r.mNeighbors)):
        # 
        for x in range(len(r.mNeighbors)):
            chance = random.randint(0, complexity)
            if x != v and chance == 1:
                r.mNeighbors[v].append(x)  
    return r


def main():
    x = 700
    y = 700
    
    win = pygame.display.set_mode((x, y))
    counter = 0
    solve = []
    with open("graphMedium.txt", 'r') as file:
        for line in file:
            if counter == 0:
                numV = int(line)
                g = Graph(numV, win, x, y)
                counter += 1
            elif counter == 1:
                numE = int(line)
                counter += 1
                temp = 0
            elif counter == 2:
                if temp < numE:
                    info = line.split()
                    e0 = int(info[0])
                    e1 = int(info[1])
                    g.addEdge(e0, e1)
                    temp += 1
                else:
                    counter += 1
                    numP = line
                    temp = 0
            elif counter == 3:
                if temp < int(numP):
                    info = line.split()
                    s0 = int(info[0]), int(info[1])
                    solve.append(s0)
                    temp += 1
                else:
                    counter += 1
            else:
                break
            
    #solve for breadth first
    for b in solve:
        b0 = b[0]
        b1 = b[1]
        path1 = g.findPathBreadth(b0, b1)

    #solve for depth first
    for d in solve:
        d0 = d[0]
        d1 = d[1]
        path2 = g.findPathDepth(d0, d1)

    #Draw graph from txt
    g.draw(win, path1)



    #create Random Graph
    #Size, window, win_width, win_height, complexity( 1: very complexy, 100: very simple)
    # 10 to 20 (5 to 10 percent) is best for smaller sizes, 20 + better for larger graphs
    g2 = randomGraph(62, win, x, y, 1)
    path3 = g2.findPathDepth(0, 62)
    path4 = g2.findPathBreadth(0, 62)
    g2.draw(win, path4)

    pygame.display.update()



    return

if __name__ == "__main__":
    main()






