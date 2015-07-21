n,m = map(int, raw_input().split())
lower_bound = int((n+1)/2)
ans = int((lower_bound+m-1)/m*m) 
if(ans>n):
	ans = -1
print ans
