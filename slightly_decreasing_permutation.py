n, k = map(int, raw_input().split())
i = n
for j in range(k):
	print n-j,
	i = i-1
for j in range(1,i+1):
	print j,
