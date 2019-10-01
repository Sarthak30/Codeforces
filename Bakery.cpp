#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("in.txt","r",stdin);
    vector<int> city;
    vector<vector<pair<int,int>>>G;
    map<int,int> yo;
    int n,m,k;
    cin>>n>>m>>k;
    G.resize(n+1);
    while(m--)
    {
        int a,b,c;
        cin>>a>>b>>c;
        G[a].push_back(make_pair(b,c));
        G[b].push_back(make_pair(a,c));
    }
    while(k--)
    {
        int temp;
        cin>>temp;
        yo[temp]=1;
        city.push_back(temp);
    }
    int ans=INT_MAX;
    for(int i=0;i<city.size();++i)
    {
        int curr=city[i];
        for(int j=0;j<G[curr].size();++j)
            if(yo.find(G[curr][j].first)==yo.end())
                ans=min(ans,G[curr][j].second);
    }
    if(ans==INT_MAX)
        cout<<"-1";
    else
        cout<<ans;
    return 0;
}
