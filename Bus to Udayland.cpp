#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("in.txt","r",stdin);
    int n;
    cin>>n;
    vector<string> yo;
    int flag=0;
    for(int i=0;i<n;++i)
    {
        string s;
        cin>>s;
        if(s[0]=='O' && s[1]=='O')
        {
            if(flag==0)
            {
                flag=1;
                s[0]=s[1]='+';
            }
        }
        if(s[3]=='O' && s[4]=='O')
        {
            if(flag==0)
            {
                flag=1;
                s[3]=s[4]='+';
            }
        }
        yo.push_back(s);
    }
    if(flag==0)
        cout<<"NO";
    else
    {
        cout<<"YES\n";
        for(int i=0;i<yo.size();++i)
            cout<<yo[i]<<"\n";
    }
    return 0;
}
