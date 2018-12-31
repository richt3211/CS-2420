a = [5, 8, 10, 58, 29, 39, 50, 38, 59, 18, 690, 49, 60, 90 ]

def quicksort(a, low, high):
	#basecase

	if high - low <= 0:
		return

	#1st pass of quicksort
	lmgt = low + 1
	for i in range(low + 1, high + 1):
		if a[i] < a[low]:
			a[i], a[lmgt] = a[lmgt], a[i]
			lmgt+= 1

	pivotindex = lmgt - 1
	a[low], a[pivotindex] = a[pivotindex], a[low]

	#recurse
	
	quickSort(a, low, pivotindex -1)
	quickSort(a, pivotindex + 1, high)
