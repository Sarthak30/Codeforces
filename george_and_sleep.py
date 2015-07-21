h, m = map(int, raw_input().split(':'))
dh, dm = map(int, raw_input().split(':'))
h -= dh
m -= dm
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
print "%02d:%02d" % (h, m)
