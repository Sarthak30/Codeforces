import collections
n, k = map(int, raw_input().split())
a = raw_input().split()
ans = 0
for i in a:
	counter = collections.Counter(str(i))
	luck = 0
	for j in counter:
		if(j=='4' or j=='7'):
			luck = luck + counter[j]
	if(luck<=k):
		ans = ans + 1
print ans
