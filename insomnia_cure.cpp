#include<stdio.h>
int main()
{
	unsigned int k,l,m,n,d;
	unsigned int i;
	unsigned int count=0;
	scanf("%d",&k);
	scanf("%d",&l);
	scanf("%d",&m);
	scanf("%d",&n);
	scanf("%d",&d);
	for(i=1;i<=d;i++)
	{
		if(i%k==0)
		{
			count++;
			continue;
		}
		if(i%l==0)
		{
			count++;
			continue;
		}
		if(i%m==0)
		{
			count++;
			continue;
		}
		if(i%n==0)
		{
			count++;
			continue;
		}
	}
	printf("%d",count);
	return 0;
}
