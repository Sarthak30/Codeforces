#include<stdio.h>
#include<iostream>
using namespace std;

long int removez(long int n)
{
	int dig,t=0;
	int i = 1;
	while(n)
	{
		dig = n%10;
		n = n/10;
		if(dig)
		{
			t = t+dig*i;
			i = i*10;
		}
	}
	return t;
}

int main()
{
	long int a,b,c,x,y,z;
	cin>>a;
	cin>>b;
	c = a+b;
	x = removez(a);
	y = removez(b);
	z = removez(c);
	if(z == (x+y)) cout<<"YES";
	else cout<<"NO";
	return 0;
}
