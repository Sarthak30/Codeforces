n,m = map(int,raw_input().split())
mi=(n-m+1)*(n-m)/2;
ma=((n%m)*(int(n/m)+1)*(int(n/m))/2)+((m-n%m)*(int(n/m))*(int(n/m)-1)/2);
print ma,
print mi
