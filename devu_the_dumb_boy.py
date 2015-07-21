n, x = map(int,raw_input().split())
a = sorted(map(int,raw_input().split()))
t = 0
for i in a:
	t = t+(x*i)
	if(x==1):
		continue
	x = x-1
print t
