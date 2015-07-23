#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

int toggle(int n)
{
	if(n==1) return 0;
	if(n==0) return 1;
}

int main()
{
	int a[3][3];
	int b[3][3] = {1,1,1,1,1,1,1,1,1};
	int i,j;
	for (i=0;i<3;i++)
	{
		for (j=0;j<3;j++)
		{
			cin>>a[i][j];
		}
	}
	for (i=0;i<3;i++)
	{
		for (j=0;j<3;j++)
		{
			if(a[i][j]%2 != 0)
			{
				b[i][j] = toggle(b[i][j]);
				if((i+1)<3) b[i+1][j] = toggle(b[i+1][j]);
				if((i-1)>-1) b[i-1][j] = toggle(b[i-1][j]);
				if((j+1)<3) b[i][j+1] = toggle(b[i][j+1]);
				if((j-1)>-1) b[i][j-1] = toggle(b[i][j-1]);
			}
		}
	}
	for (i=0;i<3;i++)
	{
		for (j=0;j<3;j++)
		{
			cout<<b[i][j];
		}
		cout<<"\n";
	}
	return 0;
}
