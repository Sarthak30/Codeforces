n, m = map(int,raw_input().split())
a = map(int,raw_input().split())
ans = 0
while len(a)!=0:
	d = m
	ans = ans+1
	while(len(a)!=0 and d>=a[0]):
		d = d-a[0]
		a.pop(0)
print ans
