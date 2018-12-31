a = [3, 4,9, 1,2,0,89,34,54,234,45,234,3,4,6]

def quicksort(a, low, high, mod):
	#basecase
	if high - low <= 0:
		return
	#do 1 pass of quicksort
	if mod:
		mid = high / 2
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
	if mod:
		quicksort(a, low, pivotindex - 1, True )
	else:
		quicksort(a, low, pivotindex -1, False)

	#righthalf
	if mod:
		quicksort(a, pivotindex + 1, high, True )
	else:
		quicksort(a, pivotindex + 1, high, False )

quicksort(a, 0, len(a) - 1, False)
print (a)
