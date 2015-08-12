raw_input()
a = map(int,raw_input().split())
c = f = 0
for i in a:
	if(a[i] == i):
		c = c+1
	elif(a[a[i]] == i):
		f = 1
ans = min(len(a),c+f+1)
print ans
		
