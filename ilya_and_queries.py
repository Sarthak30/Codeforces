R=raw_input
s=R()+'?'
n=len(s)-1
c=[0]*(n+1)
for i in range(n):c[i+1]=c[i]+(s[i]==s[i+1])
for _ in range(input()):
  a,b=map(int,R().split())
  print c[b-1]-c[a-1]
