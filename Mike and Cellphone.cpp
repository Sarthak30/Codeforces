#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    int n;
    cin>>n;
    string s;
    cin>>s;
    int pressed[10]={0};
    for(int i=0;i<s.size();++i)
        pressed[s[i]-'0']=1;
    if((pressed[1] || pressed[2] || pressed[3]) && pressed[0])
        cout<<"YES";
    else if((pressed[1] && pressed[9]) || (pressed[3] && pressed[7]))
        cout<<"YES";
    else if( (pressed[1] && pressed[3]) && (pressed[7] || pressed[9]))
        cout<<"YES";
    else if(pressed[2] && pressed[7] && pressed[9])
        cout<<"YES";
    else if(pressed[7] && ( (pressed[6] && (pressed[1] || pressed[2] || pressed[3])) || (pressed[5] && pressed[3])))
        cout<<"YES";
    else if(pressed[9] && ((pressed[5] && pressed[1]) || (pressed[4] && (pressed[1] || pressed[2] ||pressed[3])) ))
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}
