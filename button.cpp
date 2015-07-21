#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    long long int n, cnt=0, i=0;
    scanf("%I64d", &n);
    while(n>0) {
        cnt+=n+(n-1)*i;
        n--, i++;
    }
    printf("%I64d", cnt);
    return 0;
}
