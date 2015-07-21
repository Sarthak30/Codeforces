n,m = map(int, raw_input().split())
i = 0
while(n>0):
	n = n-1
	i = i+1
	if(i%m==0):
		n=n+1
print i
	
