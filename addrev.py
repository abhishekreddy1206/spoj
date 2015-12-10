x,y,sum=[],[],[]
cases=input()

def reverse(n):
	return int(str(n)[::-1])

for i in range(0,cases):
	a = raw_input().split()
	x.append(a[0])
	y.append(a[1])
	sum.append(reverse(reverse(x[i])+reverse(y[i])))

print '\n'.join(map(str,sum))