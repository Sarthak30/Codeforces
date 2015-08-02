#include<stdio.h>
int p1[1000001],p2[1000001];
int main()
{
	int n,k1,k2,i,it=0,ans=0;
	scanf("%d",&n);
	scanf("%d",&k1);
	for(i=0;i<k1;i++)
		scanf("%d",&p1[i]);
	scanf("%d",&k2);
	for(i=0;i<k2;i++)
		scanf("%d",&p2[i]);
	int f1=0,r1=k1-1,f2=0,r2=k2-1;
	while(it<=1000)
	{
//		printf("in loop\n");
		it++;
		if(p1[f1]>p2[f2])
		{
			r1++;
			p1[r1]=p2[f2];
			f2++;
			r1++;
			p1[r1]=p1[f1];
			f1++;
		}
		else
		{
			r2++;
			p2[r2]=p1[f1];
			f1++;
			r2++;
			p2[r2]=p2[f2];
			f2++;
		}
		if(f1>r1)
		{
			ans=2;
			break;
		}
		if(f2>r2)
		{
			ans=1;
			break;
		}
	}
		if(ans)
			printf("%d %d\n",it,ans);
		else printf("-1\n");
	return 0;
}
