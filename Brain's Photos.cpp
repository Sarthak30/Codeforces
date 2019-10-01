#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    int n,m;
    cin>>n>>m;
    bool flag=true;
    for(int i=0;i<n;++i)
    {
        for(int j=0;j<m;++j)
        {
            string temp;
            cin>>temp;
            if(temp[0]=='C' || temp[0]=='M' || temp[0]=='Y')
                flag=false;
        }
    }
    if(flag==true)
        cout<<"#Black&White";
    else
        cout<<"#Color";
    return 0;
}
