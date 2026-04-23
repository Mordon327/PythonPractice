def fizzbuzz(numbers = 100): 
	for num in range(1, numbers):
		if num % 3 == 0 and num % 5 == 0:
			print(f"Fizzbuzz {num}"),
		elif num % 3 == 0:
			print(f"Fizz {num}"),
		elif num % 5 == 0:
			print(f"buzz {num}"),
		else:
			print(num)