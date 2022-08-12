#4.1
numbers = []
for number in range(1,21):
	print(number)
	numbers.append(number)
print(numbers)
#4.2
print(sum(numbers))
#a large number
numbers = []
for number in range(1,1000001):
	numbers.append(number)
print(sum(numbers))
#odd numbers
numbers = [2*value-1 for value in range(1, 11)]
print(numbers)

odd_numbers = []
for value in range(1, 21):
	odd_numbers.append(value)
for even in range(2, 21, 2):
	odd_numbers.remove(even)
print(odd_numbers)

#multiple of three
three = [3*value for value in range(11)]
print(three)

three = []
for value in range(11):
	three.append(3*value)
print(three)

#cubes
cubes = [value**3 for value in range(10)]
print(sum(cubes))

#inverse
inverse = [1/(2)**value for value in range(1,19)]
print(sum(inverse))
#exponential
import math

print(2*math.pi*7)
print(math.pi)
expo = [1/math.pi**value for value in range(1,10)]
print(sum(expo))
expo_2 = [1/value**value for value in range(1,15)]
print(expo_2)
print(sum(expo_2))
