#include<bits/stdc++.h>
using namespace std;
vector< vector<int> > G;
#define INF INT_MAX
int dist[200001];
void bfs()
{
    queue<int> Q;
    Q.push(1);
    while(Q.empty()==false)
    {
        int node=Q.front();
        Q.pop();
        for(int i=0;i<G[node].size();++i)
        {
            int curr=G[node][i];
            if(dist[curr]>dist[node]+1)
            {
                Q.push(curr);
                dist[curr]=dist[node]+1;
            }
        }
    }
}
int main(void)
{
    freopen("in.txt","r",stdin);
    int n;
    cin>>n;
    G.resize(n+1);
    for(int i=1;i<n;++i)
    {
        G[i].push_back(i+1);
    }
    for(int i=n;i>1;--i)
    {
        G[i].push_back(i-1);
    }
    for(int i=1;i<=n;++i)
    {
        dist[i]=INF;
        int temp;
        cin>>temp;
        if(i!=temp)
            G[i].push_back(temp);
    }
    dist[1]=0;
    bfs();
    G.clear();
    for(int i=1;i<=n;++i)
        cout<<dist[i]<<" ";

    return 0;
}
