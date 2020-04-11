print("fibonacci number? ")
num = int(input())

def fibo(n):
	if(n == 0):
		return 1;
	elif(n == 1):
		return 1;
	else:
		return fibo(n-2) + fibo(n-1)

result = []

for i in range(num):
	result.append(fibo(i))

print("F", num, " = ", result)


