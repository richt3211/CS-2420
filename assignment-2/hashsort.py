a = [2,7,6,3,2,4,1,2,4]
print a
def hashsort(a):

	frequency = []
	for i in range(len(a)):
		frequency.append(0)
	for i in range(len(a)):
		frequency[a[i]] += 1
	count = 0
	for i in range(len(frequency)):
		for j in range(frequency[i]):
			a[count] = i
			count += 1



hashsort(a)