n = int(raw_input())
c = map(int,raw_input().split())
e = max(c)
l = min(c)
e = c.index(e)
d = e
e = c.pop(e)
c = [e]+c
c = c[::-1]
l = c.index(l)
print l+d
