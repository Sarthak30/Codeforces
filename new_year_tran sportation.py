n,t = map(int,raw_input().split())
c = map(int,raw_input().split())
i=1
flag=0
while(i<=t):
	if(i==t):
		print "YES"
		flag=1
		break
	else:
		i=i+c[i-1]
if(flag==0):
	print 'NO'		
