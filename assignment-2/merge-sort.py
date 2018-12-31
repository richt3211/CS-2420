a = [3,8,1,5,6,2,4, 7]

def mergeSort(a):
	#basecase
	if len(a) <=1:
		return
	#split
	l = a[0: len(a)/2]
	r = a[len(a)/2: len(a)]
	#recurse
	mergeSort(l)
	mergeSort(r)

	#merge l and r back onto a
	print ("left list: " + str(l))
	print ("right list: "+ str(r))
	i = 0
	j = 0
	k = 0
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
mergeSort(a)
print a
	