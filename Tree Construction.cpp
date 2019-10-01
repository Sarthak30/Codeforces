#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin>>n;
    set<int> yo;
    map<int,int> right,left;
    int temp;
    cin>>temp;
    yo.insert(temp);
    for(int i=1;i<n;++i)
    {
        cin>>temp;

        auto it=yo.lower_bound(temp);
        if(it==yo.end())
        {
            --it;
            right[*it]=1;
            cout<<*it<<" ";
        }
        else
        {
            if(left[*it])
            {
                --it;
                right[*it]=1;
                cout<<*it<<" ";
            }
            else
            {
                left[*it]=1;
                cout<<*it<<" ";
            }
        }
        yo.insert(temp);
    }
    return 0;
}
