#printing values 1-20
for value in range(1,21):
	print(value)

#making a list with values from 1-1,000,000 then printing each individually
numbers = list(range(1, 1_000_001))
for value in numbers:
	print(value)

#summing 1,000,000 numbers
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#list with odd numbers 1-20 then printing with for loop
odd_numbers = list(range(1,20,2))
for value in odd_numbers:
	print(value)

#list with multiples of 3 from 3-30 then print each
three_multiples = list(range(3,31,3))
for value in three_multiples:
	print(value)

#cubing 1-10 and printing
cubes = list(range(1,11))
for value in cubes:
	cube = value**3
	print(cube)

#list of cubed values 1-10 with list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)