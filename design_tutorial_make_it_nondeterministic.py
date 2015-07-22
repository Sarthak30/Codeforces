n = int(raw_input())
s = []
for i in range(0,n):
    x,y = raw_input().split()
    s.append((x,y))
a = map(int,raw_input().split())
y = ""
flag = 0
x = min(s[a[0]-1])
for i in range(1,n):
    l = a[i]-1
    if s[l][0]>x and s[l][1]>x:
       y = min(s[l])
       x = y
    elif s[l][0]>x or s[l][1]>x:
       y = max(s[l])
       x = y
    else:
        flag = 1
        break
if flag == 0:
    print "YES"
else:
    print "NO"
