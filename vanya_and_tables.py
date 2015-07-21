n = int(raw_input())
ans = 0
for i in range(n):
    x1, y1, x2, y2 = map(int, raw_input().split())
    ans += (x2 - x1 + 1) * (y2 - y1 + 1)
print ans
