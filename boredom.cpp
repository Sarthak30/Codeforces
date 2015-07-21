#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,st,end) for(int i=st;i<end;i++)
#define db(x) cout << (#x) << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define MAX 100005
typedef long long int ll;
ll dp[MAX];
ll count1[MAX];
int main(){
	int n,x;
	cin>>n;
	REP(i,n){
		cin>>x;
		count1[x]++;
	}
	dp[0]=0;
	dp[1]=count1[1];
	for(int i=2;i<MAX;i++){
		dp[i]=max(dp[i-1],dp[i-2]+i*count1[i]);
	}
	cout<<dp[MAX-1];
}
