n = int(raw_input())
s = str(raw_input())
a = sum(map(int,list(s[:n/2])))
b = sum(map(int,list(s[n/2:])))
c = list(set(s))
if(c==['4','7'] or c==['7','4'] or c==['4'] or c==['7']) and a==b:
	print "YES"
else:
	print "NO"
