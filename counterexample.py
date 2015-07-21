l, r = map(int,raw_input().split())
if(l%2!=0):
	l = l+1
if(l+2>r):
	print "-1"
else:
	print l,
	print l+1,
	print l+2
	
