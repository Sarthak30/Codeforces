a = str(raw_input())
flag=0
b=a.find('h')
if(b==-1):
	print "NO"
	flag=1
if(flag==0):
	a = a[b+1:]
	c = a.find('e')
	print 
	if(c==-1):
		print "NO"
		flag=1
if(flag==0):
	a = a[c+1:]
	d = a.find('l')
	if(d==-1):
		print "NO"
		flag=1
if(flag==0):
	a = a[d+1:]
	e = a.find('l')
	if(e==-1):
		print "NO"
		flag=1
if(flag==0):
	f=a[e+1:].find('o')
	if(f==-1):
		print "NO"
		flag=1
if(flag==0):
	print "YES"
