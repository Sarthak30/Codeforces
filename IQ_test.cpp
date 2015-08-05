#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int i, j;
	char arr[4][4];
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cin>>arr[i][j];
		}
	}
	int count;
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			count = 0;
			if(arr[i][j+1]=='#') count++;
			if(arr[i+1][j]=='#') count++;
			if(arr[i+1][j+1]=='#') count++;
			if(arr[i][j]=='#') count++;
			if(count == 0 || count == 4 || count == 3 || count == 1)
			{
				cout<<"YES";
				return 0;
			}
		}
		
	}
	cout<<"NO";
	return 0;
}
