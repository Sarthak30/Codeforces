import collections
c = 0
c1 = 0
raw_input()
a = map(int,raw_input().split())
counter = collections.Counter(a)
for i in counter:
	if(i<1):
		continue
	if(counter[i]==2):
		c = c+1
	if(counter[i]>=3):
		print '-1'
		exit()
if(c1 == len(a)):
	print "0"
	exit()
print c
