a, b, s = map(int,raw_input().split())
if(a<0):
	a = a*-1
if(b<0):
	b = b*-1
if (a+b<=s) and ((s-(a+b))%2==0):
	print "Yes"
else:
	print "No"
