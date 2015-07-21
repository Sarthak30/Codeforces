n = int(raw_input())
if(n%2!=0):
	print "-1"
	exit()
for i in range(1,n,2):
	print str(i+1)+" "+str(i),
