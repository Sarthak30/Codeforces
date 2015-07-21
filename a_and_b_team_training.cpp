#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double EPS = 1e-9;
const double PI = acos(-1.0);
const int MOD = 1000 * 1000 * 1000 + 7;
const int INF = 2000 * 1000 * 1000;

template <typename T>
inline T sqr(T n) {
    return n * n;
}

int n, m, ans;

int main() {
#ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
#endif

    scanf("%d%d", &n, &m);

    for (int i = 0; i <= n; i++) {
        int cur = i;
        int leftn = n - i;
        int leftm = m - 2 * i;

        if (leftm >= 0) {
            cur += min(leftm, leftn / 2);
            ans = max(ans, cur);
        }
    }

    printf("%d\n", ans);
    
    return 0;
}
