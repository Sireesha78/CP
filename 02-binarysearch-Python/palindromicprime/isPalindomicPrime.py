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
def Palindrom(n):
	temp=n
	rev=0
	while(n>0):
		rem=n%10
		rev=rev*10+rem
		n=n//10
	if(temp==rev):
		return True
	else:
		return False
	return isPrime(Palindrom)
def isPalindromicPrime(x):
    if(isPrime(x) and Palindrom(x)):
        return True
    else:
        return False