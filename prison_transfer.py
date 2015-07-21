n, t, c = map(int,raw_input().split())
a = map(int,raw_input().split())
i = 0
ans = 0
while True:
	j = i
	while(j<n):
		if(a[j]<=t):
			j = j+1
			continue
		else:
			ans = ans + max(j-i -c +1,0)
			i = j+1
			break
	if(j==n):
		ans = ans + max(j-i -c +1,0)
		break
print ans
