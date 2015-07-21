a = int(raw_input())
b = str(raw_input())
i=0
j=1
count=0
while(i<a-1 and j<a):
	if(b[i]==b[j]):
		count=count+1
		j=j+1
	else:
		j=j+1
		i=j-1
print count
