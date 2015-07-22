n = int(raw_input())
c = []
x = []
y = []
for i in range(n):
	a = map(int,raw_input().split())
	c.append(a)
	x.append(a[0])
	y.append(a[1])
xsum = sum(x)
ysum = sum(y)
if(xsum%2 == 0 and ysum%2 == 0):
	print "0"
	exit()
if ((xsum%2==0 and ysum%2!=0) or (xsum%2!=0 and ysum%2==0)):
	print "-1"
	exit()
for i in c:
	if((i[0]%2==0 and i[1]%2!=0) or (i[0]%2!=0 and i[1]%2==0) ):
		print "1"
		exit()
print "-1"
