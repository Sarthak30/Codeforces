#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>
using namespace std;
static int arr[5000001];
void ini()
{
    int i;
    for(i=2;i<=5000000;++i)
    {
        if(arr[i]==0)
        {
            arr[i]=1;
            int j;
            for(j=i*2;j<=5000000;j+=i)
            {
                int kaka=0;
                int temp=j;
                while(j%i==0)
                {
                    ++kaka;
                    j=j/i;
                }
                j=temp;
                arr[j]+=kaka;
            }
        }
    }
    for(i=3;i<=5000000;++i)
        arr[i]+=arr[i-1];

}
int main(void)
{
    ini();
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        int ans=arr[a]-arr[b];
        printf("%d\n",ans);
    }
    return 0;
}
