n = int(raw_input())
c = [0,0,0]
for i in range(n):
	a = map(int,raw_input().split())
	c[0] = c[0]+a[0]
	c[1] = c[1]+a[1]
	c[2] = c[2]+a[2]
if(c[0]==0 and c[1]==0 and c[2]==0):
	print "YES"
else:
	print "NO"
