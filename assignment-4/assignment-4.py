import sys
import datetime

class Student:

	def __init__(self, last, first, ssn, email):
		self.mLast = last
		self.mFirst = first
		self.mSsn = ssn
		self.mEmail = email
	def __eq__(self, rhs):
		if self.mSsn == rhs.mSsn:
			return True
		else:
			return False

def main():
	with open(sys.argv[1], 'r') as file:
		first_line = file.readline().split()
		first_student = Student(first_line[0],first_line[1], first_line[2], first_line[3])
		students = [first_student]
		start = datetime.datetime.now()
		for line in file:
			add_student = True
			data = line.split()
			new_student = Student(data[0], data[1], data[2], data[3])
			for student in students:
				if new_student == student:
					print ("Cannot add " + str(new_student.mFirst) + str(new_student.mLast))
					add_student = False
			if add_student:
				students.append(new_student)
		end = datetime.datetime.now()
		time = end - start
		print (len(students))
		print("Time: " + str(time))

if __name__ == "__main__":
	main()