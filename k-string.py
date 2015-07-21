import collections
n = int(raw_input())
m = list(raw_input())
counter = collections.Counter(m)
l = len(m)
str = ''
for i in counter:
	if(counter[i]%n != 0):
		print '-1'
		exit()
	str=str+i*(counter[i]/n)
print str*(n)
