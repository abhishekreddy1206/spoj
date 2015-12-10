x = [False]*1000
y = range(1,1001)

for i in y:
	z = y[i-1::i]
	for j in z:
		x[j-1] = not x[j-1]
		
print x.count(True)
print x.count(False)