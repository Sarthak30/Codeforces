a = "CODEFORCES"
ok = False
s = raw_input()
for i in range(len(a)+1):
    if s.startswith(a[:i]) and s.endswith(a[i:]):
        ok = True
        break
if ok == True:
	print "YES"
else:
	print "NO"
