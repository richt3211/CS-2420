#heaps are most often represented as lists, but we need to be able to find their parents

parent = (child -1) // 2
childL = parent * 2 + 1
childR = p * 2 + 2

#need to be able to insert and delete from heaps in tree form. 


# for graph assignment need to use queue

from collections import deque

q = deque()
q.append(item)
item = q.popleft()