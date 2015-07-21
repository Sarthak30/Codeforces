p, n = map(int,raw_input().split())
a = []
for i in range(n):
	x = int(raw_input())
	if(x%p in a):
		print i+1
		exit()
	else:
		a.insert(0,x%p)
print '-1'
