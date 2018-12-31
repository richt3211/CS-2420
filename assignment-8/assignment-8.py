import hashtable
import sys
import datetime

class Student:

	def __init__(self, last, first, ssn, email, age):
		self.mLast = last
		self.mFirst = first
		self.mSsn = ssn
		self.mEmail = email
		self.mAge = age
	def __eq__(self,rhs):
		if self.mSsn == rhs.mSsn:
			return True
		else:
			return False
	def __lt__(self, rhs):
		if self.mSsn < rhs.mSsn:
			return True
		else:
			return False
	def __gt__(self, rhs):
		if self.mSsn > rhs.mSsn:
			return True
		else:
			return False
	def __int__(self):
		return int(self.mSsn.replace('-', ''))


	def getAge(self):
		return self.mAge

def insertNames():
	with open(sys.argv[1], 'r') as file:
		start = datetime.datetime.now()
		students = hashtable.UUC(3000000)
		failures = 0
		for line in file:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			if students.insert(student) == False:
				failures +=1
		end = datetime.datetime.now()
		time = end - start
		print("Inserting")
		print("time of insertion: " , time)
		print("Successes: ", students.getSize())
		print("Failures: ", failures)
		print()
		return students
gTOTAL_AGE = 0
def addAges(s):
	global gTOTAL_AGE
	gTOTAL_AGE += int(s.getAge())
def deleteNames(students):
	with open(sys.argv[2], 'r') as file:
		start = datetime.datetime.now()
		success = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy_student = Student( 0, 0, data, 0, 0)
			if students.delete(dummy_student) == False:
				failures += 1
			else:
				success += 1
		end = datetime.datetime.now()
		time = end - start
		print("Deleting")
		print("Time of deletion: ", time)
		print("successes: ", success)
		print("failures ", failures)
		print()
def retrieveNames(students):
	with open(sys.argv[3], 'r') as file:
		start = datetime.datetime.now()
		total_age = 0
		total_students = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy = Student(0,0,data,0,0)
			studentR = students.retrieve(dummy)
			if studentR:
				total_age += int(studentR.getAge())
				total_students +=1
			else:
				failures += 1
		avg_age = total_age / total_students
		end = datetime.datetime.now()
		time = end - start
		print("Retrieving:")
		print("time of retrieval: ", time)
		print("success: ", total_students)
		print("failures: ", failures)
		print("avg age: ", avg_age)
		print()
def traverseNames(students):
	start = datetime.datetime.now()
	students.traverse(addAges)
	avg_age = gTOTAL_AGE / students.getSize()
	end = datetime.datetime.now()
	time = end - start
	print("Traversing")
	print("Time of traversal: ", time) 
	print("Avg Age: " , avg_age)
	print()
def main():
	students = insertNames()
	traverseNames(students)
	deleteNames(students)
	retrieveNames(students)

if __name__ == "__main__":
	main()
	
