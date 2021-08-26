def isPrime(x):
	if (x < 2):
		return False
	if (x == 2):
		return True
	if (x % 2 == 0):
		return False
	n= round(x**0.5)

	for i in range(3,n+1,2):
		if (x % i == 0):
			return False
		
	return True
def sum(s):
	sum=0
	while(s > 0):
		a=int(s % 10)
		s = int(s // 10)
		sum= sum+a
	return isPrime(sum)