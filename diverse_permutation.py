n,k=map(int,raw_input().split())
s=[x+1 for x in range(n)]
for i in range(1,k+1):
    if (i%2==0):
        s[i]=i/2+1
    else:
        s[i]=k+1-(i-1)/2
print " ".join(map(str,s))
