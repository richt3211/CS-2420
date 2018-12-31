import random
import sys

def main():
	# bubble
	for sort in (real_quick_sort, modified_quick_sort, mergesort, hashsort):
		test_array = [4,7,2,1,8,3,9,5]
		a = createRandomList(10)
		b = a[: ]
		print (a)
		sort(a)
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
def real_quick_sort(a):
	quicksort(a, 0, len(a) - 1, False)
def modified_quick_sort(a):
	quicksort(a, 0, len(a) - 1, True)

def quicksort(a, low, high, mod):
	#basecase
	if high - low <= 0:
		return
	#do 1 pass of quicksort
	if mod:
		mid = int((high + low) / 2)
		a[low], a[mid] = a[mid], a[low]
	lmgt = low + 1
	for i in range(low+ 1, high + 1):
		if a[i] < a[low]:
			a[i], a[lmgt] = a[lmgt], a[i]
			lmgt +=1

	pivotindex = lmgt - 1
	a[low] , a [pivotindex] = a[pivotindex], a[low]

	#recurse

	#lefthalf
	quicksort(a, low, pivotindex - 1, mod )
	#righthalf
	quicksort(a, pivotindex + 1, high, mod )



def mergesort(a):
	#basecase
	if len(a) <=1:
		return
	#split
	l = a[0: int(len(a)/2)]
	r = a[int(len(a)/2): int(len(a))]
	#recurse
	mergesort(l)
	mergesort(r)

	#merge l and r back onto a
	i = 0
	j = 0
	k = 0
	# print(a)
	while (len(l) -1 ) >= i and (len(r) -1) >=j:
		if l[i] <= r[j]:
			a[k] = l[i]
			i+= 1
			k+= 1
		else:
			a[k] = r[j]
			j+= 1
			k+= 1
	while (len(l) -1) >= i:
		a[k] = l[i]
		i+=1
		k+=1
	while (len(r) -1) >= j:
		a[k] = r[j]
		j+=1
		k+=1
	# print(a)
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
if __name__ == "__main__":
	main()