c = map(int,raw_input().split())
b = str(raw_input())
s = 0
for i in b:
	s = s + c[int(i)-1]
print s
