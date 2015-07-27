x, y = map(int, raw_input().split())
s = abs(x)+abs(y)
if x>0 and y>0:
    print 0,s,s,0
if x>0 and y<0:
    print 0,-s,s,0
if x<0 and y>0:
    print -s,0,0,s
if x<0 and y<0:
    print -s,0,0,-s
