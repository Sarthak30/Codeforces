n = int(raw_input())
As = map(int, raw_input().split())

prev = 0

ii = 0
for i in range(n):
    if As[i] < prev:
        ii = i
        break
    prev = As[i]

newAs = As[ii:] + As[:ii]
if newAs == sorted(As):
    print (n - ii) % n
else:
    print -1
