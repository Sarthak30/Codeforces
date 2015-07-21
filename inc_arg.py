n = int(raw_input())
a = str(raw_input())
a = a[::-1]
c = int(a,2)
b = c+1
b = bin(b)[2:]
if(len(b)>n):
    b = b[::-1]
    b = b[:n]
    b = b[::-1]
elif(len(b)<n):
	x = 2**(n-len(b))
	x = bin(x)[3:]
	b = x+b
b = int(b,2)
a = int(a,2)
print bin(a^b).count('1')
