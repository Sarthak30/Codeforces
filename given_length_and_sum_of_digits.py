m,s=map(int,raw_input().split())
a,b,c,d=(s-1)/9,(s-1)%9,s/9,s%9
def P(x):
  return 10*P(x-1) if x>0 else 1
if 9*m<s or m>1 and s<1:
  print -1,-1
elif s<1:
  print 0,0
else:
  print P(m-1)+b*P(a)+P(a)-1,(P(c)-1)*P(m-c)+d*P(m-c-1)
