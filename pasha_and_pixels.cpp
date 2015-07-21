#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;
#define pf printf
#define sf scanf
#define MAX 1005

int sq[MAX][MAX];

int main()
{
    int n, m, k;
    int i, j, t, temp;
    sf("%d%d%d", &n, &m, &k);
    temp =0;
    for(t=1; t<=k; t++)
    {
        sf("%d%d", &i, &j);
        sq[i][j] = 1;
        if(!temp)
        {
            if(sq[i][j+1]==1 && sq[i+1][j] ==1 && sq[i+1][j+1]==1)
            {
                temp = t;
            }
            else if(sq[i][j+1]==1 && sq[i-1][j]==1 && sq[i-1][j+1]==1)
            {
                temp = t;
            }
            else if(sq[i][j-1]==1 && sq[i-1][j]==1 && sq[i-1][j-1]==1)
            {
                temp = t;
            }
            else if(sq[i][j-1]==1 && sq[i+1][j-1]==1 && sq[i+1][j]==1)
            {
                temp = t;
            }
        }
        else
        {
            break;
        }
    }
    pf("%d\n", temp);
    return 0;
}
