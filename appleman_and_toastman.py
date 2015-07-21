a = int(raw_input())
c = map(int,raw_input().split())
c.sort()
d = len(c)
result = 0
for i in range(0,d-1):
	result = result + (i+2)*c[i]
result = result + c[-1]*a
print result
