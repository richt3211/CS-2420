a = [6,3,8,1,4,2,7]

def selection(a):
	for i in range(len(a) -1 ):
		smallest = i
		for j in range(smallest + 1, len(a)):
			if a[j] < a[smallest]:
				smallest = j
		a[i], a[smallest] = a[smallest], a[i]
	
selection(a)
print (a)
