total,diff,x,y=[],[],[],[]

for i in xrange(0,10):
	total = int(input())
	diff = int(input())
	z=(total+diff)/2
	x.append(z)
	y.append(total-z)

for i in xrange(0,10):
	print x[i]
	print y[i]