#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("in.txt","r",stdin);
    string s;
    cin>>s;
    int ans=0;
    char pos='a';
    for(int i=0;i<s.size();++i)
    {
        char curr=s[i];
        int a=((pos-curr)+26)%26;
        int b=((curr-pos)+26)%26;
        ans+=min(a,b);
        pos=curr;
    }
    cout<<ans;
    return 0;
}
