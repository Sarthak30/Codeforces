#include<bits/stdc++.h>
using namespace std;
vector<vector<int>>G;
struct node
{
    int a;
    int b;
    int temp;
    int i;
};
vector<node> arr;
bool shelf[1005][1005]={false};
bool invert[1005]={0};
int ans[100504]={0};
int cnt[1005]={0};
int m;
void dfs(int idx,int total_books)
{
    bool flag=false;
    int a=arr[idx].a;
    int b=arr[idx].b;
    int temp=arr[idx].temp;
    int index=arr[idx].i;
    if(temp==1)
    {
        if(shelf[a][b]==invert[a])
        {
            flag=true;
            cnt[a]++;
            shelf[a][b]=!invert[a];
            total_books++;
        }
    }
    else if(temp==2)
    {
        if(shelf[a][b]==!invert[a])
        {
            flag=true;
            cnt[a]--;
            shelf[a][b]=invert[a];
            total_books--;
        }
    }
    else if(temp==3)
    {
        invert[a]=!invert[a];
        total_books-=cnt[a];
        cnt[a]=m-cnt[a];
        total_books+=cnt[a];
    }
    ans[index]=total_books;
    for(int i=0;i<G[idx].size();++i)
        dfs(G[idx][i],total_books);

    if(temp==1)
    {
        if(flag==true)
        {
            cnt[a]--;
            total_books--;
            shelf[a][b]=invert[a];
        }
    }
    else if(temp==2)
    {
        if(flag==true)
        {
            cnt[a]++;
            shelf[a][b]=!invert[a];
            total_books++;
        }
    }
    else if(temp==3)
    {
        total_books-=cnt[a];
        cnt[a]=m-cnt[a];
        invert[a]=!invert[a];
        total_books+=cnt[a];
    }
}
int main(void)
{
    freopen("in.txt","r",stdin);
    int n,q;
    cin>>n>>m>>q;
    G.resize(100050);
    arr.push_back({0,0,0,0});
    for(int i=0;i<q;++i)
    {
        int temp;
        cin>>temp;
        int a,b=0;
        if(temp<=2)
            cin>>a>>b;
        else
            cin>>a;
        arr.push_back({a,b,temp,i+1});
        if(temp==4)
            G[a].push_back(i+1);
        else
            G[i].push_back(i+1);
    }
    dfs(0,0);
    G.clear();
    for(int i=1;i<=q;++i)
        cout<<ans[i]<<endl;
    return 0;
}
