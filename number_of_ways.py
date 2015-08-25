n=input()
a=map(int,raw_input().split())
s=sum(a)
w=0
if not s%3:
  s=s/3
  t=s*2
  u,g=0,0
  for x in a[:-1]:
    u+=x
    if u==t:
      w+=g
    if u==s:
      g+=1
print w
