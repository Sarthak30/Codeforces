n, m, k = map(int,raw_input().split())
b = []
count = 0
for i in range(m+1):
	b.append(int(raw_input()))
for i in range(m):
	b[i] = bin(b[i]^b[-1])
	if(b[i].count('1') <= k):
		count = count + 1
print count 
