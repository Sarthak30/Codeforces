n, k = map(int,raw_input().split())
y = map(int,raw_input().split())
z = sorted(y)
k = 5-k
if(k<0):
	print "0"
else:
	count = 0
	for i in z:
		if(i<=k):
			count = count+1
print int(count/3)
