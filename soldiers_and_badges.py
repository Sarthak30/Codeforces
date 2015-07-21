n = int(raw_input())
b = sorted(map(int,raw_input().split()))
c = 0
s = 0
for i in b:
	c = max(c+1,i)
	s = s+c
print s - sum(b)
