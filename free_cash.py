import collections
a = int(raw_input())
c=[]
for i in range(0,a):
	c.append(str(raw_input()))
counter = collections.Counter(c)
print max(counter.values())
