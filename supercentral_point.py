
n = input()
pts = [map(int, raw_input().split()) for i in range(n)]
ans = 0
for p in pts:
    if any(p[0]==q[0] and p[1]<q[1] for q in pts) \
    and any(p[0]==q[0] and p[1]>q[1] for q in pts) \
    and any(p[0]<q[0] and p[1]==q[1] for q in pts) \
    and any(p[0]>q[0] and p[1]==q[1] for q in pts):
        ans += 1
print ans
