n=input()
a=[[0,0,0] for _ in range(10**6+1)]
for i,x in enumerate(map(int,raw_input().split())):
	if a[x][0]==0: a[x][2]=i
	a[x][1]=i-a[x][2]
	a[x][0]-=1
ans=min(a)
print ans[2]+1,ans[1]+ans[2]+1
