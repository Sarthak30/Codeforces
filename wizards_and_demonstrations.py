n, x, y = map(int, raw_input().split())
a = float(n)*float(y)/100.0
c = str(a).split('.')
a = int(a)
if(int(c[1]) != 0):
	a = a+1
if(a-x)<0:
	print "0"
else:
	print a-x
