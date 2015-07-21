n,m=map(int,raw_input().split())
a=map(int,raw_input().split())
b=[0]*100001
c=[0]*100001
ans=0
for i in range(n-1,-1,-1):
    if b[a[i]]==0:
        ans+=1
        b[a[i]]=1
    c[i+1]=ans
for i in range(m):
    q=input()
    print c[q]
