a = str(raw_input())
d = a[1:-1]
b = d.split(', ')
if (len(a)==2):
	print "0"
else:
	c = list(set(b))
	print len(c)
