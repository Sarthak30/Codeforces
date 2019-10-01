#include<iostream>
using namespace std;
int check(long long yo,long long n)
{
    if(yo>=1 && yo<=n)
        return 1;
    else
        return 0;
}
int main(void)
{
    long long n,a,b,c,d,ans=0,u,v,x,y;
    cin>>n>>a>>b>>c>>d;
    for(long long i=1;i<=n;++i)
    {
        u=i;
        v=u+b-c;
        x=u+a-d;
        y=u+a+b-d-c;
        if(check(v,n) && check(x,n) && check(y,n))
            ans+=n;
    }
    cout<<ans;
    return 0;
}
