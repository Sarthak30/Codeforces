#include<iostream>
#include<cstdio>
using namespace std;
int A[100001],B[100001];
int possible(int ans,int n,int k)
{
    int st=0,en=st+ans-1,flag=0;
    while(en<n)
    {
        if(st==0)
        {
            if((min(A[en],B[en]))<=k)
            {
                flag=1;
                break;
            }
        }
        else
        {
            if(min(A[en]-A[st-1],B[en]-B[st-1])<=k)
            {
                flag=1;
                break;
            }
        }
        st++;
        en++;
    }
    return flag;
}
int main(void)
{
    freopen("in.txt","r",stdin);
    string yo;
    int n,k;
    cin>>n>>k;
    cin>>yo;
    if(yo[0]=='a')
        A[0]++;
    else
        B[0]++;
    for(int i=1;i<yo.size();++i)
    {
        if(yo[i]=='a')
            A[i]++;
        else
            B[i]++;
        A[i]+=A[i-1];
        B[i]+=B[i-1];
    }
    int ans_lo=1,ans_hi=n,ans_mid;
    while(ans_lo<ans_hi)
    {
        ans_mid=(ans_lo+ans_hi)/2;
        if(possible(ans_mid,n,k))
            ans_lo=ans_mid+1;
        else
            ans_hi=ans_mid-1;
    }
    if(!possible(ans_hi,n,k))
        ans_hi--;
    cout<<ans_hi;
    return 0;
}
