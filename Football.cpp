#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	char d[15];
	char b[15], c[15];
	int a[2] = {0};
	int n;
	cin>>n;
	cin>>b;
	strcpy(d,b);
	a[0]++;
	n--;
	while(n--)
	{
		cin>>b;
		if(strcmp(b,d)==0) a[0]++;
		else 
		{
			a[1]++;
			strcpy(c,b);
		}
	}
	if(a[0]>a[1]) cout<<d;
	else cout<<c;
	return 0;
}
		
