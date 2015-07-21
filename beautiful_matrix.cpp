#include<stdio.h>
int main()
{
	int m[5][5];
	for(int i=0; i<5; i++)
	{
		for(int j=0; j<5; j++)
		{
			scanf("%d",&m[i][j]);
		}
	}
	int flag=0;
	int p,q;
	for(int i=0;i<5;i++)
	{
		for(int j=0;j<5;j++)
		{
			if(m[i][j]==1)
			{
				flag = 1;
				p = i;
				q = j;
				break;
			}
		}
		if(flag==1)
			break;
	}
	int x = (2-p);
	int y = (2-q);
	if(x<0)
	{
		x = -x;
	}
	if(y<0)
	{
		y = -y;
	}
	printf("%d",x+y);
	return 0;
}
