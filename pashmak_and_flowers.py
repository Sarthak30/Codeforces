n = int(raw_input())
b = map(int,raw_input().split())
x = max(b)
y = min(b)
z = x-y
print z,
if(x==y):
	print n*(n-1)/2
else:
	t1 = 0
	t2 = 0
	for i in range(n):
		 t1 += (b[i] == y)
		 t2 += (b[i] == x);
	print t1*t2
