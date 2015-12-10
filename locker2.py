x = [False]*1000
y = range(1,1001)

for i in y:
	if i%2 == 0:
		z1 = y[::-1]
		z = z1[i-1::i]
		for j in z:
			x[j-1] = not x[j-1]
	else:
		z = y[i-1::i]
		for j in z:
			x[j-1] = not x[j-1]
		
print x.count(True)
print x.count(False)