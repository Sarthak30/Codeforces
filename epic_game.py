from fractions import gcd
a,b,n = map(int,raw_input().split())
i = 0
j = 0
while(i==0):
	if(j%2==0):
		if(n>gcd(n,a)):
			n=n-gcd(a,n)
		else:
			print "0"
			break
	else:
		if(n>gcd(b,n)):
			n=n-gcd(b,n)
		else:
			print "1"
			break 
	j=j+1
