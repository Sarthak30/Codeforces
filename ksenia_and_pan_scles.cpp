#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	char a[1000],b[1000];
	cin>>a;
	cin>>b;
	int x,y;
	x = strlen(a);
	y = strlen(b);
	if((x+y-1)%2!=0)
	{
		cout<<"Impossible";
		return 0;
	}
	char left[1000],right[1000];
	int i = 0;
	while(a[i]!='|')
	{
		left[i] = a[i];
		i++;
	}
	left[i] = '\0';
	i++;
	int j=0;
	while(a[i]!='\0')
	{
		right[j] = a[i];
		j++;	i++;
	}
	right[j] = '\0';
	int w,v;
	w = strlen(left);
	v = strlen(right);
	while(y>0)
	{
		if(w<v)
		{
			left[w] = b[y-1];
			w++;
			y--;
		}
		else
		{
			right[v] = b[y-1];
			v++;
			y--;
		}
	}
	right[v]='\0';
	if(w==v)
	{
		cout<<left;
		cout<<'|';
		cout<<right;
	}
	else
	{
		cout<<"Impossible";
	}
	return 0;
}
