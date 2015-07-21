n, m = map(int,raw_input().split())
i = 1
while(m>=i):
	m = m-i
	i = i+1
	if(i==n+1):
		i = 1
print m
