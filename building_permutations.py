n = int(raw_input())
a = map(int,raw_input().split())
a.sort()
j = 1
ans = 0
for i in a:
	ans = ans + abs(j-i)
	j = j+1
print ans
