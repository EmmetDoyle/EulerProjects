res = 0
factor = 2
num = 600851475143

def isPrime(num):
	if num == 2 or num == 3:
		return True
	else:
		for i in range(2,num):
			if num % i == 0:
				return False
		return True

while isPrime(int(num)) == False:
	solved = False
	factor = 2
	while solved == False:
		if isPrime(factor):
			if num % factor == 0:
				print(factor)
				if factor > res:
					res = factor
				solved = True
				num = num/factor
		factor += 1

if num > res:
	res = num

print (res)
