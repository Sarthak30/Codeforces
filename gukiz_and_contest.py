n = int(raw_input())
a = map(int,raw_input().split())
b = sorted(a, reverse=True)
c = []
for i in a:
	print (b.index(i)+1),
