list1 = [2, 6, 3, 1, 9, 5, 8]
list2 = [1,2,3,4,6,8,9]

def linearsearch(list, value):
	for x in range(len(list1)):
		if list[x] == value:
			return x
	else:
		return -1
value = linearsearch(list1, 9)
print value

def binarysearch(list, value):

	low = 0
	high = len(list2) - 1 
	while low <= high:
		mid = (low + high) / 2
		if list2[mid] == value:
			return mid
		elif value < list2[mid]:
			high = mid - 1
		else:
			value > list2[mid]
			low = mid + 1
	return - 1
value = binarysearch(list2, 8)
print value 
