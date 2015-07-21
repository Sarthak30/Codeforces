a = int(raw_input())
flag = 0
for i in range(a):
	b = float(raw_input())
	n = 360.0/(180-b)
	f = int(n)
	if(f==n):
		print "YES"
	else:
		print "NO"	
