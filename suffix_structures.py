s, t = raw_input(), raw_input()
u, v = sorted(s), sorted(t)
def subset(a, b):
    i = 0
    for c in a:
        if i < len(b) and c == b[i]: i += 1
    return i == len(b)
if u == v: print "array"
elif subset(s, t): print "automaton"
elif subset(u, v): print "both"
else: print "need tree"
