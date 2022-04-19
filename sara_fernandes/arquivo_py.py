n = 100000000

def result(n: int):
	result = 0
	for i in range(1, n+1):
		result += i 
	return result

print(result(n))

def result_n(n):
	return n*(n+1)/2

print(result_n(n))
