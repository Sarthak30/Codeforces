#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("in.txt","r",stdin);
    int n;
    cin>>n;
    vector<int> arr;
    for(int i=0;i<n;++i)
    {
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    sort(arr.begin(),arr.end());
    int q;
    cin>>q;
    while(q--)
    {
        int m;
        cin>>m;
        vector<int>::iterator it=upper_bound(arr.begin(),arr.end(),m);
        cout<<it-arr.begin()<<"\n";
    }
    return 0;
}
