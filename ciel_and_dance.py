n, m = map(int,raw_input().split())
print n+m-1
for i in range(1,n+1):
	print str(i)+" "+'1'
for i in range(2,m+1):
	print '1'+" "+str(i)
	
