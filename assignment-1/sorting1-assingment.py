import random
import sys

def main():
	# bubble
	c = [10,2,3,4,5,6,7,8,9,1]
	a = createRandomList(10)
	b = a[: ]
	print(c)
	bubbleSort(c)
	print (a)
	b.sort()
	print(b)
	print()
	if a != b:
		print("Too bad, try again")
	# shaker
	d = [10,2,3,4,5,6,7,8,9,1]
	a = createRandomList(10)
	print(d)
	b = a[: ]
	shakerSort(d)
	print(d)
	b.sort()
	print(b)
	print()
	if a != b:
		print("Too bad, try again")
	#selection
	a = createRandomList(10)
	print(a)
	b = a[: ]
	selectionSort(a)
	print(a)
	b.sort()
	print(b)
	print()
	if a != b:
		print("Too bad, try again")


def createRandomList(n):
	a = []
	for i in range(n):
		r = random.randrange(0,n)
		a.append(r)
	return a
def bubbleSort(a):
	done = False
	while done == False:
		done = True
		for i in range(len(a) - 1):
			if a[i] > a[i + 1]:
				done = False
				a[i], a[i + 1] = a[i+1], a[i]
				print (a)
		print ()
	return a
def shakerSort(a):
	done = False
	while done == False:
		done = True
		for i in range(len(a) - 1):
			if a[i] > a[i + 1]:
				done = False
				a[i], a[i + 1] = a[i+1], a[i]
				print (a)
		print ("Going left to right")
		if done == True:
			break
		done = True
		for i in range(len(a) - 2 , -1, -1):
			if a[i] > a[i + 1]:
				done = False
				a[i], a[i + 1] = a[i+1], a[i]
				print (a)
		print ("Going right to left")
		if done == True:
			break
	return a
def selectionSort(a):
	for i in range(len(a) -1 ):
		smallest = i
		for j in range(smallest + 1, len(a)):
			if a[j] < a[smallest]:
				smallest = j
		a[i], a[smallest] = a[smallest], a[i]
		# print (a)
if __name__ == "__main__":
	main()