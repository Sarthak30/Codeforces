#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    map<long long,int> yo;
    int n;
    cin>>n;
    int ans=n-1;
    long long int sum=0;
    for(int i=0;i<n;++i)
    {
        long long int temp;
        cin>>temp;
        sum+=temp;
        yo[sum]++;
        ans=min(ans,n-yo[sum]);
    }
    cout<<ans;
    return 0;
}
