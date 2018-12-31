def traverse(self, callback):
	for item in self.mTable:
		if item:
			callback(item)

def trueSize(self):
	count = 0
	for item in self.mTabl:
		if item:
			count += 1
	return count

def retrieve(self, dummy):
	index = int(dummy) % self.mTable.size()
	while self.mTable[index] is not None:
		if self.mTable[index] and self.mTable[index] == dummy:
			return self.mTable[index]
		index +=1
	return None

def delete(self,dummy):
	if not self.exists(item)
