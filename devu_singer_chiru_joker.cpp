#include<bits/stdc++.h>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int SZ(const T&c) { return c.size(); }

const int N = (int) 1e2 + 100;

int a[N];

int main() {
    int n, d, sum = 0;
    cin >> n >> d;

    REP(i,n)
    {
        cin >> a[i];
        sum += a[i];
    }

    if (sum + 10 * (n - 1) > d)
        cout << -1 << endl;
    else
        cout << (d - sum) / 5 << endl;

      return 0;
}
