a = str(raw_input())
n = len(a)
i = 0
while(i<n):
	if n-i>=3 and a[i] is '1' and a[i+1] is '4' and a[i+2] is '4':
		i = i+3
	elif n-i>=2 and a[i] is '1' and a[i+1] is '4':
		i = i+2
	elif a[i] is '1' :
		i = i+1
	else:
		print "NO"
		exit()
print "YES"

