import collections
n, k = map(int,raw_input().split())
a = raw_input()
counter = dict(collections.Counter(a))
counter = sorted(list(counter.values()),reverse = True)
i = 0
ans = 0
while (i<k and (i+counter[0])<k):
	i = i+counter[0]
	ans = ans+(counter[0]*counter[0])
	counter.pop(0)
if(i != k and len(counter)>0):
	i =k-i
	ans = ans+(i*i)
print ans
