n,m = map(int,raw_input().split())
f = [list(raw_input()) for j in range(n)]
#print f
for i in range(n):
	for j in range(m):
		if f[i][j] == ".":
			if ((i%2) ^ (j%2)):
				f[i][j] = "W"
			else:
				f[i][j] = "B"
	print "".join(f[i]) 
