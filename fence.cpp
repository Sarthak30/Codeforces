#include<stdio.h>
int main()
{
	int n,k,i;
	scanf("%d%d",&n,&k);
	int a[150000];
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	int max=0;
	for(i=0;i<k;i++)
		max=max+a[i];
	int pos=0,val=max;
	for(i=1;i<n-k+1;i++)
	{
		val=val-a[i-1]+a[i+k-1];
		if(val<max)
		{
			max=val;
			pos=i;
		}
	}
	printf("%d\n",pos+1);
	return 0;
}
