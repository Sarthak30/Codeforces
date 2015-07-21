a = int(raw_input())
p = 0
c = []
for i in range(0,a):
	a,b = map(int, raw_input().split())
	p = p-a
	p = p+b
	c.append(p)
print max(c)
	
