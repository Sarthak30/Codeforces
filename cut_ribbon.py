n,a,b,c = map(int,raw_input().split())
dp=[0]+[-1e9]*5000
for i in xrange(1,n+1):
    dp[i]=max(dp[i-a],dp[i-b],dp[i-c])+1
print dp[n]
