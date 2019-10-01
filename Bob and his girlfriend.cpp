#include<stdio.h>
#include<string.h>
int min(int a,int b)
{
	if(a<b)
		return a;
	else
		return b;
}
char a[2001],b[2001];
int dp[2001][2001];
void func(char *a,char *b)
{
	int len1=strlen(a);
	int len2=strlen(b);
	int i;
	for(i=0;i<=len1;++i)
		dp[i][0]=i;
	for(i=0;i<=len2;++i)
		dp[0][i]=i;
	int j;
	for(i=1;i<=len1;++i)
	{
		for(j=1;j<=len2;++j)
		{
			if(a[i-1]==b[j-1])
			{
				dp[i][j]=dp[i-1][j-1];
				continue;
			}
			dp[i][j]=min(dp[i-1][j-1]+1,min(dp[i-1][j]+1,dp[i][j-1]+1));
		}
	}
	printf("%d\n",dp[len1][len2]);	
}
int main(void)
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s %s",a,b);
		func(b,a);
	}
	return 0;
}
