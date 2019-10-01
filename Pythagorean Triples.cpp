#include<bits/stdc++.h>
using namespace std;
bool isPerfect(long long temp)
{
    long long sq=sqrt(temp);
    if(sq*sq==temp)
        return true;
    else
        return false;
}
int main(void)
{
    long long num;
    cin>>num;
    if(num>2 && num%2==0)
    {
        num/=2;
        cout<<num*num-1<<" "<<num*num+1;
        return 0;
    }
    if(num>2 && isPerfect(num+1))
    {
        long long yo=sqrt(num+1);
        cout<<2*yo<<" "<<yo*yo+1;
        return 0;
    }
    if(num>2 && isPerfect(num-1))
    {
        long long yo=sqrt(num-1);
        cout<<2*yo<<" "<<yo*yo-1;
        return 0;
    }
    if(num>2)
    {
        cout<<(num*num+1)/2<<" "<<(num*num-1)/2;
        return 0;
    }
    cout<<"-1";
    return 0;
}
