en,x0,y0=map(int,raw_input().split())
r=0
dic={}
for i in range(en):
    x,y=map(int,raw_input().split())
    if x!=x0:
        t=float(y-y0)/float(x-x0)
        dic[t]=1
    else:
         r=1
for a in dic:
    r+=dic[a]
print r
