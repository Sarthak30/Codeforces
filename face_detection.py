I=lambda:map(int,raw_input().split())
n,m=I()
g= [raw_input() for _ in xrange(n)]

k=0
for x in range(n-1):
	for y in range(m-1):
		if {g[x][y],g[x][y+1],g[x+1][y],g[x+1][y+1]} == set('face'): k+=1
print k
