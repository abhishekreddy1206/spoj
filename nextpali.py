output = []
cases = input()

def next_higher(K):
    if all(digit == '9' for digit in K):
        return int(K) + 2
    L = len(K)
    left = K[:L/2]
    center = L % 2 and K[L/2] or ""
    right = left[::-1]
    P = left + center + right
    if P > K:
        return P
    if center and center != '9':
        center = chr(ord(center) + 1)
        return left + center + right
    elif center:
        center = '0'
    left = list(left)
    digits_left = len(left)
    while digits_left:
        idx = digits_left - 1
        if left[idx] == '9':
            left[idx] = '0'
            digits_left = digits_left - 1
        else:
            left[idx] = chr(ord(left[idx]) + 1)
            break
    left = "".join(left)
    right = left[::-1]
    return left + center + right

for i in range(0,cases):
    z = raw_input()
    output.append(next_higher(z))

for i in range(0,cases):
    print output[i]