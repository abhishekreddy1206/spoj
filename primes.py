# x,y=[],[]
# 
# def genprime(start, end):
#     return list(sorted(set(range(start,end+1)).difference(set((p * f) for p in range(2, int(end ** 0.5) + 2) for f in xrange(2, (end/p) + 1)))))
# 
# for test in range(0,cases = int(input())):
# 	a,b = raw_input().split()
# 	x.append(int(a))
# 	y.append(int(b))
# 
# for test in range(0,cases):
# 	result = genprime(x[test], y[test])
# 	for z in result:
# 		print z

########################################

# final=[]
# 
# for i in xrange(int(input())):
#     start,end=[int(x) for x in raw_input().split()]
#     if start==1:
#         start=2
#     # sieve of eras** algorithm
#     final.append(list(sorted(set(xrange(start,end+1)).difference(set((p * f) for p in xrange(2, int(end ** 0.5) + 2) for f in xrange(2, int(end/p) + 1))))))
# 
# 
# # print final list items
# for item1 in final:
#     print("\n".join([str(x) for x in item1]))
#     print('\n')

#########################################

from math import sqrt
primes = [2]

for i in range(3,32000,2):
    isprime = True

    cap = sqrt(i)+1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break
    if (isprime):
        primes.append(i)

T = input()
output = ""
for t in range(T):

    if (t > 0):
        output += "\n"

    M,N = raw_input().split(' ')
    M = int(M)
    N = int(N)
    cap = sqrt(N)+1

    if (M < 2):
        M = 2

    isprime = [True]*100001

    for i in primes:
        if (i >= cap):
            break

        if (i >= M):
            start = i*2
        else:
            start = M + ((i - M % i)%i)

        # The two below, obscure lines create a continuous
        #  block of false elements in order to set all
        #  elements correspnding to numbers divisible by i
        #  in isprime to be false
        # In turns out that this runs substantially faster
        #  than setting the elements individually using loops
        falseblock = [False] * len(isprime[start-M:N+1-M:i]);
        isprime[start-M:N+1-M:i] = falseblock

    for i in range(M,N+1):
        if (isprime[i-M] == True):
            output += str(i) + "\n"

print output[:-1]