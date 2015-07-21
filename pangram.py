d = {'q':0,
		'w':0,
		'e':0,
		'r':0,
		't':0,
		'y':0,
		'u':0,
		'i':0,
		'o':0,
		'p':0,
		'a':0,
		's':0,
		'd':0,
		'f':0,
		'g':0,
		'h':0,
		'j':0,
		'k':0,
		'l':0,
		'z':0,
		'x':0,
		'c':0,
		'v':0,
		'b':0,
		'n':0,
		'm':0}
		
a = int(raw_input())
b = str(raw_input())
b = b.lower()
for i in b:
	d[i] = d[i]+1
flag = 0
for i in d:
	if(d[i]==0):
		flag = 1
		print "NO"
		break
if(flag==0):
	print "YES"

