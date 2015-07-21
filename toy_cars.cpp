#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int a[101][101];
	int n;
	int count = 0;
	int b[101];
	int k = 0;
	int flag;
	cin>>n;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			cin>>a[i][j];
		}
	}
	for(int i = 0; i < n; i++)
	{
		flag = 0;
		for(int j = 0; j < n; j++)
		{
			if(a[i][j]==1 || a[i][j]==3)
			{
				flag = 1;
				break;
			}
		}
		if(flag == 0)
		{
			b[k] = i+1;
			k++;
			count++;
		}
	}
	cout<<count<<"\n";
	for(int i = 0; i < k; i++)
		cout<<b[i]<<" ";
	return 0;
}
		
