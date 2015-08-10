x,y=map(int,raw_input().split())
a,b=map(int,raw_input().split())
c,d=map(int,raw_input().split())
if (a+c<=x and b<=y and d<=y) or (a+d<=x and b<=y and c<=y) or (b+c<=x and a<=y and d<=y) or (b+d<=x and a<=y and c<=y) or (a+c<=y and b<=x and d<=x) or (a+d<=y and b<=x and c<=x) or (b+c<=y and a<=x and d<=x) or (b+d<=y and a<=x and c<=x):
    print 'YES'
else:
    print 'NO'
