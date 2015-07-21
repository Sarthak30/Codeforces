#include <cstdio>
#include <map>

using namespace std;

const int NUM = 200100;

int main() {
  int n;
  scanf("%d", &n);

  char loc[NUM];
  scanf("%s", loc);
  
  map<int, int> m;
  int rooms = (n - 1) * 2;
  int ans = 0;
  for (int i = 0; i != rooms; i += 2) {
    m[loc[i] - 'a']++;
    if (m[loc[i + 1] - 'A'] == 0) {
      ans++;
    } else {
      m[loc[i + 1] - 'A']--;
    }
  }

  printf("%d\n", ans);

  return 0;
}
