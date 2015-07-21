n = int(raw_input())
a = sorted(map(int,raw_input().split()))
m = int(raw_input())
b = sorted(map(int,raw_input().split()))
i = 0
j = 0
ans = 0
while i<n and j<m:
	if abs(a[i]-b[j])<2:
		ans = ans + 1
		i = i + 1
		j = j + 1
	elif a[i]<b[j]:
		i = i + 1
	else:
		j = j + 1
print ans
