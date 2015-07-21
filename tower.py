import collections
c = int(raw_input())
a = map(int,raw_input().split())
b = len(list(set(a)))
counter = collections.Counter(a)
print str(max(counter.values()))+" "+str(b)
