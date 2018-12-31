#implemented as a hash table
class UUC:

	def __init__(self, dataSize):
		tableSize = 2 * dataSize + 1 # making sure table size is twice the size of data as an odd number
		while not isPrime(tableSize):
			tableSize += 2 # incrementing by two so number stays odd
		self.mTable = [none] * tableSize # making the table the tablesize with all nones. 

	def Insert(self, item):
		if self.Exists(item):
			return False:
		key = int(item) # taking whatever the operator overload for the int method is and putting it as a key
		index = key % len(self.mTable)
		while self.mTable[index] is not None:
			index += 1
			if index >= len(self.mTable):
				index = 0
		self.mTable[index] = item

#operator overloading for integer so that the when casting the item to an int it returns the key value
class Student:

	def __int__(self):
		return int(self.mSsn.replace("-",""))