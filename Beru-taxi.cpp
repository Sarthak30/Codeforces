#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("in.txt","r",stdin);
    double a,b;
    cin>>a>>b;
    int n;
    cin>>n;
    double ans=999999.99999999999;
    while(n--)
    {
        double x,y,z;
        cin>>x>>y>>z;
        double xx=abs(x-a);
        xx=xx*xx;
        double yy=abs(y-b);
        yy=yy*yy;
        xx=(double)sqrt(xx+yy);
        if(xx==0)
        {
            ans=0.00000000000;
        }
        else
        {
            ans=min(ans,1.00000000*xx/z);
            //cout<<ans<<endl;
        }
    }
    printf("%.10f\n",ans);
    return 0;
}
