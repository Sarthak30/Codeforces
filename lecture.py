n, m = map(int,raw_input().split())
lang = {}
for i in range(m):
	a, b = raw_input().split()
	if(len(b)>=len(a)):
		lang[a] = a
	else:
		lang[a] = b
d = raw_input().split()
for i in d:
	print lang[i],
