n = raw_input()
t = map(int,raw_input().split())
t = sorted(t)
ans = 1
num = t[0]
for i in t[1:]:
	if(i<num):
		continue
	else:
		num = num+i
		ans = ans+1
print ans
