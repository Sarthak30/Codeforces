#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int n,i;
	cin>>n;
	if(n%2!=0)
	{
		cout<<"-1";
		return 0;
	}
	for (i=1;i<n;i=i+2)
	{
		cout<<i+1<<" "<<i<<" ";
	}
	return 0;
}
