n = int(raw_input())
i = 0
j = 0
while(j<n):
	count = 0
	a = []
	while(count<n/2):
		a.append(i+1)
		a.append((n*n)-i)
		i = i + 1
		count = count + 1
	for k in a:
		print k,
	print
	j = j + 1
