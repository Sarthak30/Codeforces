#include<bits/stdc++.h>
using namespace std;
set<int> indexes[300001];
int main(void)
{
    freopen("in.txt","r",stdin);
    int n,q;
    cin>>n>>q;
    vector< pair<int,bool> > arr;
    int ctr=0;
    int ans=0;
    int maxi=-1;
    while(q--)
    {
        int temp,a;
        cin>>temp>>a;
        if(temp==1)
        {
            arr.push_back(make_pair(a,true));
            indexes[a].insert(ctr);
            ++ctr;
            ++ans;
        }
        else if(temp==2)
        {
            for(set<int>::iterator it=indexes[a].begin();it!=indexes[a].end();++it)
            {
                if(arr[*it].second==true)
                {
                    --ans;
                    arr[*it].second=false;
                }
            }
            indexes[a].clear();
        }
        else
        {
            --a;
            if(a>maxi)
            {
                for(int i=maxi+1;i<=a;++i)
                {
                    if(arr[i].second==true)
                    {
                        --ans;
                        int lala=arr[i].first;
                        arr[i].second=false;
                        set<int>::iterator it=indexes[lala].find(i);
                        if(it!=indexes[lala].end())
                            indexes[lala].erase(it);
                    }
                }
                maxi=a;
            }
        }
        cout<<ans<<endl;
    }
    arr.clear();
    return 0;
}
