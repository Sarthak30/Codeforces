a, b = map(int,raw_input().split())
if(a%2 == 0):
	part = a/2
else:
	part = int((a/2)+1)
if(b<=part):
	print (2*b)-1
else:
	print (b-part)*2


