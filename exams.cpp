#include<bits/stdc++.h>
using namespace std;
int n, last;
pair<int, int> p[111111];
int main()
	{
	cin >> n;
	for(int i = 1; i <= n; i++)
		{
		int x, y;
		cin >> x >> y;
		p[i] = make_pair(x, y);
		}
	sort(p + 1, p + 1 + n);
	for(int i = 1; i <= n; i++)
		{
		if(last <= p[i].second)
			last = p[i].second;
		else
			last = p[i].first;
		}
	cout << last;
	}
