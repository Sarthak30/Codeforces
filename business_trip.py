k =int(raw_input())
m = map(int,raw_input().split())
m.sort(reverse=True)
count = 0
s = 0 
for i in m : 
	if(s<k):
		s=s+i
		count = count +1
	else:
		break
if(s<k):
	print -1
else:
	print count


