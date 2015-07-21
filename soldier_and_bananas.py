k, n, w = map(int, raw_input().split())
i = 1
s = 0
while(i<=w):
	s = s + i*k
	i = i+1
if(s<=n):
	print "0"
else:
	print s-n
