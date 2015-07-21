n, k = map(int,raw_input().split())
h = []
for i in range(n):
	f, t = map(int,raw_input().split())
	if(t>k):
		c = f-(t-k)
	else:
		c = f
	h.append(c)
print max(h)
