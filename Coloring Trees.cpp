#include<bits/stdc++.h>
using namespace std;
#define INF 1000000000000000
long long arr[200][200];
int color[101];
long long dp[200][200][200];
int m;
long long yo(int st,int en,int k,int prev_color,long long used,int beautyTillNow)
{
    if(st==en)
    {
        if(beautyTillNow==k)
            return used;
        else
            return LONG_MAX;
    }
    if(color[st]!=0)
    {
        if(color[st]==prev_color)
            return yo(st+1,en,k,color[st],used,beautyTillNow);
        else
            return yo(st+1,en,k,color[st],used,beautyTillNow+1);
    }
    else
    {
        long long maxi=LONG_MAX;
        for(int i=1;i<=m;++i)
        {
            if(i==prev_color)
                maxi=min(maxi,yo(st+1,en,k,i,used+arr[st][i-1],beautyTillNow));
            else
                maxi=min(maxi,yo(st+1,en,k,i,used+arr[st][i-1],beautyTillNow+1));
        }
        return maxi;
    }
}
void init()
{
    for(int i=0;i<200;++i)
        for(int j=0;j<200;++j)
            for(int k=0;k<200;++k)
                dp[i][j][k]=INF;
}
int main(void)
{
    freopen("in.txt","r",stdin);
    init();
    int n,k;
    cin>>n>>m>>k;
    for(int i=0;i<n;++i)
        cin>>color[i];
    for(int i=0;i<n;++i)
        for(int j=0;j<m;++j)
            cin>>arr[i][j];

    ///base case
    if(color[0]!=0)
        dp[0][color[0]][1]=0LL;
    else
    {
        for(int i=1;i<=m;++i)
            dp[0][i][1]=arr[0][i-1];
    }

    for(int i=1;i<n;++i)
    {
        for(int j=1;j<=m;++j)
        {
            if(color[i]!=0)
            {
                for(int x=1;x<=k;++x)
                {
                    if(j==color[i])
                        dp[i][color[i]][x]=min(dp[i][color[i]][x],dp[i-1][color[i]][x]);
                    else
                        dp[i][color[i]][x]=min(dp[i][color[i]][x],dp[i-1][j][x-1]);
                }
            }
            else
            {
                for(int l=1;l<=m;++l)
                {
                    for(int x=1;x<=k;++x)
                    {
                        if(l==j)
                            dp[i][j][x]=min(dp[i][j][x],dp[i-1][l][x]+arr[i][j-1]);
                        else
                            dp[i][j][x]=min(dp[i][j][x],dp[i-1][l][x-1]+arr[i][j-1]);
                    }
                }
            }
        }
    }
    //long long y=yo(0,n,k,-1,0LL,0);
    //y=(dp[n-1]==LONG_MAX)? -1 : y;
    long long ans=INF;
    for(int i=1;i<=m;++i)
        ans=min(ans,dp[n-1][i][k]);
    if(ans>=INF)
        cout<<"-1";
    else
        cout<<ans;
    //cout<<y;
    return 0;
}
