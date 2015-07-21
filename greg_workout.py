n = raw_input()
l=map(int,raw_input().split())
print["chest","biceps","back"][max(0,1,2,key=lambda i:sum(l[i::3]))]
