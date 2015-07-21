#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
	char a[101],b[101];
	int i,r;
	int n;
	scanf("%s",a);
	scanf("%s",b);
	n = strlen(a);
	for(i=0;i<n;i++)
	{
		a[i] = tolower(a[i]);
		b[i] = tolower(b[i]);
	}
	r=strcmp(a,b);
	if(r<0)
		printf("-1");
	else if(r>0)
		printf("1");
	else
		printf("0");
	return 0;
}
