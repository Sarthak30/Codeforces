n = int(raw_input())
c = map(int,raw_input().split())
d = []
count = 0 
for i in c:
	if i not in d:
		d.append(i)
		if(max(d)==i):
			count =count+1
		elif(min(d)==i):
			count = count+1
print (count-1)	
