#include<stdio.h>
int main()
{
	char p,c,a[21],b[21];
	int  n,no,t,s,h[2][100]={0};
	scanf("%s%s%d",a,b,&n);
	while(n--)
	{
		scanf("%d%*c%c%d%*c%c",&t,&p,&no,&c);
		s=(p=='h')?0:1;
		h[s][no]+=(c=='y')?1:2;
		if(h[s][no]>=2)
		{
			printf("%s %d %d\n",p=='h'?a:b,no,t);
			h[s][no]=-999999999;
		}
	}
	return 0;
}
