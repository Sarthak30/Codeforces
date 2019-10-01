#include<bits/stdc++.h>
using namespace std;
long long func(long long n)
{
    long long ret=0;
    long long st=2;
    while(1)
    {
        long long yo=st*st*st;
        ret+=n/yo;
        if((n/yo)==0)
            break;
        st++;
    }
    return ret;
}
int main(void)
{
    long long n;
    cin>>n;
    long long st=8,en=1e16;
    int flag=0;
    while(st<=en)
    {
        long long mid=(st+en)/2;
        long long sum=func(mid);
        if(sum==n)
        {
            flag=1;
            en=mid-1;
        }
        else if(sum<n)
            st=mid+1;
        else
            en=mid-1;
    }
    if(flag==1)
        cout<<st;
    else
        cout<<"-1";

    return 0;
}
