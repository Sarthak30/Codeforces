n = int(raw_input())
d = map(int,raw_input().split())
a, b = map(int,raw_input().split())
print sum(d[a-1:b-1])
