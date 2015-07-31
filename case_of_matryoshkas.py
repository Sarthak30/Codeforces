n, k = map(int,raw_input().split(" "))
cost = 0
for i in range(k):
	inp = map(int,raw_input().split(" "))
	m = inp[0]
	a = inp[1:]
	if a[0] != 1:
		cost += m * 2 - 1
	else:
		for j in range(m):
			if a[j] == j+1:
				continue
			j -= 1
			break
		cost += (m - j) * 2 - 1
print cost - 1
