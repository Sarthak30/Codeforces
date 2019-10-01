#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    int n;
    cin>>n;
    int flag=0;
    for(int i=0;i<n;++i)
    {
        int temp;
        cin>>temp;
        if(flag==0)
        {
            if(temp%2==0)
            {
                cout<<"1\n";
                flag=1;
            }
            else
            {
                cout<<"2\n";
                flag=0;
            }
        }
        else
        {
            if(temp%2==1)
            {
                cout<<"1\n";
                flag=1;
            }
            else
            {
                cout<<"2\n";
                flag=0;
            }
        }
    }
    return 0;
}
