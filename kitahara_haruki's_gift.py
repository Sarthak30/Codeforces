raw_input()
a=map(int,raw_input().split())
c=sum(a)
print'YES'if c%400==0 or (c%200==0 and 100 in a) else'NO'
