a = int(raw_input())
count = 0
for i in range(0,a):
	n,m = map(int,raw_input().split())
	if(m-n>=2):
		count=count+1
print count
