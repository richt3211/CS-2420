import sys

def getNumbers():
	numbers = []
	for line in sys.stdin.readlines():
		line = line.strip()
		numbers.append(line)
	return numbers
numbers = getNumbers()
def easiest(numbers):
	for number in numbers:
		if int(number) != 0:
			sum_of_input = 0 
			for i in number:
				digit = int(i)
				sum_of_input += digit
			least_good_num = 10000000
			x = 11
			done = True
			while done:
				multiple = int(number) * x
				multiple = str(multiple)
				sum_of_multiple = 0
				for i in multiple:
					sum_of_multiple += int(i)
				if sum_of_input == sum_of_multiple:
					if int(x) < int(least_good_num):
						least_good_num = x
						done = False
				x += 1
			print (least_good_num)
		else:
			return
easiest(numbers)


		