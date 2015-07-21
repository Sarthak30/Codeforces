a, b, c = map(int,raw_input().split())
ans = []
num = 0
for i in range(82):
	x = b*(i**a)+c
	if(x<=0):
		continue 
	y = sum(map(int,list(str(x))))
	if(y==i and x<1000000000):
		num = num+1
		ans.insert(0,x)
print num
ans = sorted(ans)
for i in ans:
	print i,
