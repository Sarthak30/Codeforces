import collections
c = map(int,raw_input().split())
counter = collections.Counter(c)
s = 0
d = counter.values()
for i in d:
	if(i>=2):
		s = s+i-1
print s

