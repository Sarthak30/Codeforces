#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
int isprime(int n)
{
	int x = sqrt(n);
	for(int i=2;i<=x;i++)
		if(n%i==0) return 1;
	return 0;
}
int main()
{
	int n,m;
	cin>>n>>m;
	int i;
	for(i=n+1;i<=m;i++)
	{
		if(isprime(i)==0)
		{
			if(i==m)
			{
				cout<<"YES";
				return 0;
			}
			else
			{
				cout<<"NO";
				return 0;
			}
		}
	}
	cout<<"NO";
	return 0;
}
