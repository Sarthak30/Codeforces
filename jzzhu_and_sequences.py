x, y = map(int, raw_input().split())
n = int(raw_input())
ans = [x, y, y-x, -x, -y, x-y]
print ans[(n-1) % 6] % 1000000007
