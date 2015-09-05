n,k = map(int,raw_input().split())
r = sorted([[x, -y] for x, y in [map(int, raw_input().split()) for i in range(n)]])
print r.count(r[-k])
