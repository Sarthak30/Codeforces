s=list(raw_input())
n=len(s)
f=[0]*len(s)
input()
for x in map(int,raw_input().split()):
  f[x-1]=1-f[x-1]
t=0
for i in range(n/2):
  f[i]=t^f[i]
  t=f[i]
  if t:
    s[i],s[n-1-i]=s[n-1-i],s[i]
print ''.join(s)
