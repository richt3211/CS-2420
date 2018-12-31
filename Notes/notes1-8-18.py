list1 = [5, -1, -2, 4, 5, -2, -9, 2, 1 ,-1, 3, -2, 6, 2, -3, 4, -6, -7, 4, 3, -2, 4]


def MaxSubsequence(list1):
	best = list1[0]
	start = 0
	end = 0
	for s in range(len(list1)):
		for e in range(len(list1)):
			sublist = list1[s, e]
			sumof = sum(sublist)
			if sumof > best:
				best = sumof
				start = e
				end = s
	return start, end

MaxSubsequence(list1)

1  2
2  4
3  8
4  16
5  32
6  64
7  128
8  256
9  512
10 1k

2^13 = 8k
2^25 = 32m
2^47 = 128t
2^8 = 256
2^16 = 64k
2^31 = 2b
2^39 = 528b
2^12 = 4k
2^24 = 16m
2^0 = 1