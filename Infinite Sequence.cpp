#include<iostream>
using namespace std;
int main(void)
{
    int a,b,c;
    cin>>a>>b>>c;
    int yo=b-a;
    if(c==0)
    {
        if(yo==0)
            cout<<"YES";
        else
            cout<<"NO";
    }
    else
    {
        if(yo%c)
            cout<<"NO";
        else
        {
            yo=yo/c;
            yo++;
            if(yo>0)
                cout<<"YES";
            else
                cout<<"NO";
        }
    }
    return 0;
}
