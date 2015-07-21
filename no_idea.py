n, m = map(int,raw_input().split())
c = map(int,raw_input().split())
a = map(int,raw_input().split())
b = map(int,raw_input().split())
ans = 0
for i in c:
	if i in a:
		ans = ans+1
	elif i in b:
		ans = ans -1
print ans
