a = int(raw_input())
if(a<3):
	print "-1"
	exit()
for i in range(a,a/2,-1):
	print i,
for i in range(1,a/2+1):
	print i,

"""

Tester Function

raw_input()
b = map(int,raw_input().split())
for i in range(len(b)-1):
	for j in range(i,len(b)-1):
		if(b[j]>b[j+1]):
			b[j], b[j+1] = b[j+1], b[j]
print b

"""
