#include<stdio.h>
#include<string.h>
int main()
{
	char a[101];
	scanf("%s",a);
	int n = strlen(a);
	if(n==1)
	{
		printf("%c",a[0]);
		return 0;
	}
	int b0=0,b1=0,b2=0;
	for(int i=0; i<n; i++)
	{
		if(a[i]=='1')
		{
			b0++;
		}
		else if(a[i]=='2')
		{
			b1++;
		}
		else if(a[i]=='3')
		{
			b2++;
		}
	}
	int j=0;
	char d[51];
	for(int i = 0; i<b0;i++)
	{
		d[j]='1';
		j++;
	}
	for(int i = 0; i<b1;i++)
	{
		d[j++]='2';
	}
	for(int i = 0; i<b2;i++)
	{
		d[j++]='3';
	}
	n=j;
	for(j=0;j<n-1;j++)
		printf("%c+",d[j]);
	printf("%c",d[n-1]);
	return 0;
}
