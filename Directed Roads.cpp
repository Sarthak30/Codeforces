#include<bits/stdc++.h>
#define MOD 1000000007
using namespace std;
int padosi[200500];
vector<int> faltu,cycle;
map<int,int> yo;
bool visited[200500]={false};
bool visited2[200500]={false};
long long _pow(long long base,long long exp)
{
    long long ret=1LL;
    while(exp)
    {
        if(exp%2)
            ret=(ret*base)%MOD;
        base=(base*base)%MOD;
        exp=exp/2;
    }
    return ret%MOD;
}
void dfs(int start,int node,int num)
{
    if(visited[node]==false)
    {
        visited[node]=true;
        yo[node]=num;
        dfs(start,padosi[node],num+1);
    }
    else
    {
        if(start==node)
            cycle.push_back(num-1);
        else
        {
            if(yo[node]>0)
            {
                cycle.push_back(num-yo[node]);
                faltu.push_back(yo[node]-1);
            }
            else
                faltu.push_back(num-1);
        }
    }
}
void dfs2(int node)
{
    if(visited2[node]==false)
    {
        visited2[node]=true;
        yo[node]=0;
        dfs2(padosi[node]);
    }
}
int main(void)
{
    freopen("in.txt","r",stdin);
    faltu.clear();
    cycle.clear();
    int n;
    cin>>n;
    for(int i=1;i<=n;++i)
    {
        int temp;
        cin>>temp;
        padosi[i]=temp;
    }
    for(int i=1;i<=n;++i)
    {
        if(visited[i]==false)
        {
            dfs(i,i,1);
            dfs2(i);
        }
    }
    /*for(int i=0;i<faltu.size();++i)
        cout<<"faltu "<<faltu[i]<<"\n";
    for(int i=0;i<cycle.size();++i)
        cout<<"cycle "<<cycle[i]<<"\n";
    */
    long long ans=1LL;
    for(int i=0;i<cycle.size();++i)
    {
        long long temp=(_pow(2,cycle[i])-2+MOD)%MOD;
        ans=ans*temp;
        ans%=MOD;
    }
    for(int i=0;i<faltu.size();++i)
    {
        long long temp=(MOD+_pow(2,faltu[i]))%MOD;
        ans=ans*temp;
        ans%=MOD;
    }
    cout<<ans%MOD;
    return 0;
}
