a = raw_input()
if(len(a)==1):
	if(a.islower()):
		a = a.upper()
	else:
		a = a.lower()
elif((a[0].islower() and a[1:].isupper())):
	b = a[0]
	c = a[1:]
	c = c.lower()
	b = b.upper()
	a = b+c
elif(a.isupper()):
	a = a.lower()
print a
