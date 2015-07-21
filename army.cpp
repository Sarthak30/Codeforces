#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int n, d[101], a, b, i;
	scanf("%d",&n);
	for (i=0;i<n-1;i++)
	{
		cin>>d[i];
	}
	int sum=0;
	cin>>a>>b;
	for (i=a-1;i<b-1;i++)
	{
		sum = sum+d[i];
	}
	cout<<sum;
	return 0;
}
