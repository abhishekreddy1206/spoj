fact=[]
cases=input()

def factorial(n):
	return reduce(lambda x,y:x*y,[1]+range(1,n+1))

for i in range(0,cases):
	a = input()
	fact.append(factorial(a))

print '\n'.join(map(str,fact))