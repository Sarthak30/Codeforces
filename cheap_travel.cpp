#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    long long int n,m,a,b;
    cin>>n>>m>>a>>b;
    long long int k=n/m;
    long long int ans=n*a;
    for(int i=0;i*m<2*n;i++)
    {
        int r=n-m*i;
        if(r<0) r=0;
        ans=min(ans,r*a+i*b);
    }
    if(n%m==0)
        ans=min(ans,k*b);
    else
        ans=min(ans,(k+1)*b);
    cout<<ans<<endl;
    return 0;
}
