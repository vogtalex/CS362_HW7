def printFizz(input):
	if (input % 3 == 0 and input % 5 == 0):
		return "FizzBuzz"
	if (input % 3 == 0):
		return "Fizz"
	if (input % 5 == 0):
		return "Buzz"
	return input


count = 1
while (count <= 100):
	var = printFizz(count)
	print(var)
	count += 1