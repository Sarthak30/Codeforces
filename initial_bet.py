a = map(int,raw_input().split())
b = sum(a)
if(b==0 or not(b%5==0)):
	print "-1"
elif (b%5)==0:
	print str(b/5)
