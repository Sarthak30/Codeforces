n = int(raw_input())
x = []
y = []
for i in range(n):
	x1, y1 = map(int, raw_input().split())
	x.append(x1)
	y.append(y1)
ymin = min(y)
xmin = min(x)
ymax = max(y)
xmax = max(x)
ox = xmax - xmin
oy = ymax - ymin
s = max(ox,oy)
print s*s
