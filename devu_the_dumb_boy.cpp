#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
	int n, x, a[100001], i;
	unsigned long int t;
	cin>>n>>x;
	for (i = 0; i<n ; i++)
	{
		cin>>a[i];
	}
	sort(a,a+n);
	for (i = 0; i<n ; i++)
	{
		t = t+(x*a[i]);
		if(x==1) continue;
		x = x-1;
	}
	cout<<t;
	return 0;
}
	
