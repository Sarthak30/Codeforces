a = raw_input()
b = a
flag1 = 0
flag2 = 0
if(a.find('AB')!=-1):
	a = a.replace('AB','#',1)
	if(a.find('BA')!=-1):
		flag1 = 1
if(b.find('BA')!=-1):
	b = b.replace('BA','#',1)
	if(b.find('AB')!=-1):
		flag2 = 1	
if( flag1 == 0 and flag2 == 0):
	print "NO"
else:
	print "YES"
