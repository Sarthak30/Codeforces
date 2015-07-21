#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int main()
{
	int n,i,j;
	char a[301][301];
	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
		for (j=0;j<n;j++)
		{
			cin>>a[i][j];
		}
	}
	if(n==1)
	{
		printf("YES");
		return 0;
	}
	char x = a[0][0];
	char y = a[0][1];
	if(x==y)
	{
		printf("NO");
		return 0;
	}
	for (i=0;i<n;i++)
	{
		for (j=0;j<n;j++)
		{
			if(i==j || j==(n-i-1))
			{
				if(a[i][j]!=x)
				{
					printf("NO");
					return 0;
				}
			}
			else
			{
				if(a[i][j]!=y)
				{
					printf("NO");
					return 0;
				}
			}
		}
	}
	printf("YES");
	return 0;
}
