a = (int(raw_input()))
if(a<-1):
	a = a*-1
	b = a%10
	c = a/10
	d = c/10
	e = (d*10)+b
	if(c<e):
		a=c
	else:
		a=e
	a = a*-1
print a
