#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
	int n, d, m, a[110];
	cin>>n>>d;
	int i;
	int s = 0;
	for (i=0;i<n;i++)
	{
		cin>>a[i];
	}
	sort(a,a+n);
	cin>>m;
	int x;
	if(n<m) x = n;
	else x = m;
	for(i=0;i<x;i++)
	{
		s = s+a[i];
	}
	int left = m-n;
	if(left<0) left = 0;
	int ans = s - (left*d);
	cout<<ans;
	return 0;
}
