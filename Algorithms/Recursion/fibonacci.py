def fibonacci(n):
	print("Find fibonacci for ",n)
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-2)+fibonacci(n-1)
		
print(fibonacci(10))