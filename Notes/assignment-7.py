import bst
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
		if self.mSsn < rhs.Ssn:
			return True
		else:
			return False
	def __gt__(self, rhs):
		if self.mSsn > rhs.Ssn:
			return True
		else:
			return False

def insertNames():
	with open(sys.argv[1], 'r') as file:
		start = datetime.datetime.now()
		first_line = file.readline().split()
		first_student = Student(first_line[0], first_line[1], first_line[2], first_line[3], first_line[4])
		students = bst.UUC()
		students.insert(first_student)
		failures = 0
		for line in file:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			if students.exists(student):
				failures +=1
			else:
				students.insert(student)
		end = datetime.datetime.now()
		time = end - start
		print("time of insertion: " , time)
		print("Successes: ", students.getSize())
		print("Failures: ", failures)
		return students
def main():
	students = insertNames():

