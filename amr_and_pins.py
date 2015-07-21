import math
r, x, y, x1, y1  = map(int,raw_input().split())
d = math.ceil(math.hypot(x-x1, y-y1))
print int(math.ceil(d/(2*r)))

