def main ():
	a = createRandomList(10)
	b = a[: ]
	bubblesort(a)
	b.sort(a)
	if a!= b:
		print ("Not equal")
	a = createRandomList(10)
	b = a[: ]
	bubblesort(a)
	b.sort(a)
	if a!= b:
		print ("Not equal")
	shakersort(a)

list1 = [2,8,3,1,9,3,6,2,3,5]

def bubbleSort(a):
	done = False
	while done == False:
		done = True
		for i in range(len(a) - 1):
			if a[i] > a[i + 1]:
				done = False
				a[i], a[i + 1] = a[i+1], a[i]
	return a
def shakerSort(a):
	done = False
	while done == False:
		done = True
		for i in range(len(a) - 1):
			if a[i] > a[i + 1]:
				done = False
				a[i], a[i + 1] = a[i+1], a[i]
		if done == True:
			break
		for i in range(len(a) - 2 , -1, -1):
			if a[i] > a[i + 1]:
				done = False
				a[i], a[i + 1] = a[i+1], a[i]
		if done == True:
			break
	return a
bubbleSort(list1)
print (list1)

list2 = [2,84,33,31,91,3,65,3,3]
shakerSort(list2)
print(list2)

