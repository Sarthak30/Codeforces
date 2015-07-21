n = int(raw_input())
fmin, fmax = map(int,raw_input().split())
smin, smax = map(int,raw_input().split())
tmin, tmax = map(int,raw_input().split())
if n-(smin+tmin)<=fmax:
	f = n-(smin+tmin)
else:
	f = fmax
n = n-f
if n-(tmin)<=smax:
	s = n-tmin
else:
	s = smax
n = n-s
t = n
print f,s,t
