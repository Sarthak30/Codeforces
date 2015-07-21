x = 0
n, m = map(int, raw_input().split())
for a in range(0,int(n**0.5)+1):
	b = n-a*a
	if b>=0 and a+b*b==m:
		x = x+1
print x
