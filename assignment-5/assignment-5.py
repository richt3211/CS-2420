import sys
import datetime

class Student:

	def __init__(self, last, first, ssn, email, age):
		self.mLast = last
		self.mFirst = first
		self.mSsn = ssn
		self.mEmail = email
		self.mAge = age
	def __eq__(self, rhs):
		if self.mSsn == rhs.mSsn:
			return True
		else:
			return False

def insertNames():
	with open(sys.argv[1], 'r') as file:
		first_line = file.readline().split()
		first_student = Student(first_line[0],first_line[1], first_line[2], first_line[3], first_line[4])
		students = [first_student]
		start = datetime.datetime.now()
		failures = 0
		for line in file:
			add_student = True
			data = line.split()
			new_student = Student(data[0], data[1], data[2], data[3], data[4])
			for student in students:
				if new_student == student:
					print ("Error. " + str(student.mFirst) + "already exists" )
					add_student = False
					failures += 1
			if add_student:
				students.append(new_student)
		end = datetime.datetime.now()
		time = end - start
		print("Time of insertion: " + str(time))
		print ("Successes:" + str(len(students)))
		print("Failures: " + str(failures))
		return students
def insertTestNames():
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
		lines = lines[:15]
		students = []
		start = datetime.datetime.now()
		failures = 0
		for line in lines:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			students.append(student)
		end = datetime.datetime.now()
		time = end - start
		print("Time of insertion: ", time)
		print ("Successes:" + str(len(students)))
		print("Failures: " + str(failures))
		return students

def traverseNames(names):
	total_age = 0
	start = datetime.datetime.now()
	for student in names:
		total_age += int(student.mAge)
	avg_age = total_age/ len(names)
	end = datetime.datetime.now()
	time = end - start
	print (avg_age)
	print ("Time of traversal" + str(time))

def deleteNames(names):
	with open(sys.argv[2], 'r') as file:
		start = datetime.datetime.now()
		success = 0
		failures = 0
		for line in file:
			found = False
			data = line.strip()
			dummy_student = Student(0, 0, data, 0 , 0)
			for student in names:
				if dummy_student == student:
					names.remove(student)
					success += 1
					found = True
					break
			if found == False:
				failures +=1
				print("Ssn error: " + str(dummy_student.mSsn))
		end = datetime.datetime.now()
		time = end - start
		print ("Time of deletion: " + str(time))
		print ("Successes: " + str(success))
		print ("Failures: " + str(failures))
def retrieveNames(names):
	with open(sys.argv[2], 'r') as file:
		start = datetime.datetime.now()
		total_age = 0
		total_students = 0
		failures = 0
		for line in file:
			found = False
			data = line.strip()
			dummy_student = Student(0,0,data,0,0)
			for student in names:
				if dummy_student == student:
					total_age += int(student.mAge)
					total_students += 1
					found = True
			if found == False:
				failures +=1
				print("Ssn Error: " + str(dummy_student.mSsn))
		avg_age = total_age / total_students
		end = datetime.datetime.now()
		time = end - start
		print ("Average age: " + str(avg_age))
		print ("Success: " + str(total_students))
		print ("Failures: " + str(failures))
		print ("Time of retrieval: " + str(time))

def main():
	students = insertNames()
	traverseNames(students)
	# deleteNames(students)
	# retrieveNames(students)

if __name__ == "__main__":
	main()