#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("in.txt","r",stdin);
    int n;
    cin>>n;
    vector<int> smith;
    for(int i=0;i<n;++i)
    {
        int temp;
        cin>>temp;
        smith.push_back(temp);
    }
    bool ok=true;
    int pending=0;

    for(int i=0;i<n;++i)
    {
        if(pending==1)
        {
            if(smith[i]==0)
                break;
            smith[i]--;
            pending=0;
        }
        if(smith[i]%2!=0 && smith[i]!=0)
            pending=1;
        else if(smith[i]%2==0 && smith[i]!=0)
            continue;
    }
    if(pending==0)
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}

