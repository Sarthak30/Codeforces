s = int(raw_input())
a = map(int,raw_input().split())
i = 0
s1 = 0
while(s1 < s):
	s1 = s1 + a[i]
	i = i+1
	if(i==7):
		i = 0
if(i==0):
	print '7'
	exit()
print i
