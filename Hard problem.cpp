#include<bits/stdc++.h>
using namespace std;
long long dp[100100][2];
int main(void)
{
    freopen("in.txt","r",stdin);
    int n;
    cin>>n;
    vector<long long> yo;
    for(int i=0;i<n;++i)
    {
        long long temp;
        cin>>temp;
        yo.push_back(temp);
    }
    vector<string> arr;
    for(int i=0;i<n;++i)
    {
        string temp;
        cin>>temp;
        arr.push_back(temp);
    }
    dp[0][1]=yo[0];
    dp[0][0]=0;
    for(int i=1;i<n;++i)
    {
        string curr=arr[i];
        string prev=arr[i-1];
        string swap_curr=curr;
        string swap_prev=prev;
        reverse(swap_curr.begin(),swap_curr.end());
        reverse(swap_prev.begin(),swap_prev.end());

        if(curr>=prev)
            dp[i][0]=dp[i-1][0];
        else
            dp[i][0]=-1;

        if(swap_curr>=prev && dp[i-1][0]!=-1)
            dp[i][1]=dp[i-1][0]+yo[i];
        else
            dp[i][1]=-1;

        if(curr>=swap_prev && dp[i-1][1]!=-1)
        {
            if(dp[i][0]==-1)
                dp[i][0]=dp[i-1][1];
            else
                dp[i][0]=min(dp[i][0],dp[i-1][1]);
        }

        if(swap_curr>=swap_prev && dp[i-1][1]!=-1)
        {
            if(dp[i][1]==-1)
                dp[i][1]=dp[i-1][1]+yo[i];
            else
                dp[i][1]=min(dp[i][1],dp[i-1][1]+yo[i]);
        }
    }
    if(dp[n-1][0]!=-1 && dp[n-1][1]!=-1)
        cout<<min(dp[n-1][0],dp[n-1][1]);
    else if(dp[n-1][0]!=-1)
        cout<<dp[n-1][0];
    else
        cout<<dp[n-1][1];
    return 0;
}
