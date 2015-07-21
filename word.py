a = str(raw_input())
b=0
for i in a:
	if(i.isupper()):
		b = b+1
c = len(a)
d = c-b
if(d>=b):
	a = a.lower()
else:
	a = a.upper()
print a
