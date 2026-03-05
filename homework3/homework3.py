
def say_goodbye(kimiya):
	print("Goodbye,", kimiya)
say_goodbye("Kimiya")

def subtract (a, b):
	return a - b

def multiply (a, b):
	return a * b

def divide (a, b):
	return a / b

say_goodbye ("Kimiya")

def area_of_circle(radius):
	area = 3.14 * radius * radius
	print(area)

say_goodbye("Kimiya")
def what_to_wear(readings):
	return (min(readings), max(readings))
say_goodbye("Kimiya")
def is_weekend(day): 
	if day == 6 or day == 7:
		return True
	else:
		return False 
def fuel_efficiency(distance, fuel_used):
	return distance / fuel_used

def secret_code(num):
	last_digit = num % 10
	remaining = num // 10
	multiplier = 10 ** len(str(remaining))
	return last_digit * multiplier + remaining

def power(x,y):
	result = 1
	for i in range(y):
		result = result * x
	return result 

def find_min(numbers):
	minimum = numbers[0]

	for num in numbers:
		if num < minimum:
			minimum = num

	return minimum 

def find_max(numbers): 
	maximum = numbers[0]

	for num in numbers:
		if num > maximum:
			maximum = num

	return maximum
def find_min_while(numbers):
	minimum = numbers[0]
	i = 0
							
	while i < len(numbers):
		if numbers[i] < minimum:
			minimum = numbers[i]
		i += 1

	return minimum


def find_max_while(numbers):
	maximum = numbers [0]
	i = 0

	while i < len(numbers):
		if numbers[i] < minimum:
			minimum = numbers[i]
		i +=1

	return minimum

def find_max_while(numbers):
	maximum = numbers[0]
	i = 0

	while i < len(numbers):
		if numbers[i] > maximum:
			maximum = numbers[i]
		i +=1
	
	return maximum

def sum_digits(num):
	total = 0 

	while num > 0:
		total += num % 10
		num = num // 10

	return total


num = 2468
result = sum_digits(num)

print(f"The result of Calculate the Sum (6.3) with input {num} is {result}.")






