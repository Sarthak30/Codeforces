n = int(raw_input())
a = []
b = []
for i in range(n):
	x, y = map(int,raw_input().split())
	a.append(x)
	b.append(y)
a.sort(key=dict(zip(a, b)).get)
flag = 0
for i in range(n-1):
	if(a[i]>a[i+1]):
		flag = 1
		break
if(flag==0):
	print "Poor Alex"
else:
	print "Happy Alex"
