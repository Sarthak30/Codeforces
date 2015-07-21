#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int n;

int main() {
	cin >> n;

	int a = 0, b = 0, c = 0;

	bool ok = true;

	for (int i = 0; i < n; ++i) {
		int cur;
		cin >> cur;

		if (cur == 25) {
			++a;
		} else if (cur == 50) {
			if (a == 0) ok = false;
			else {
				--a;
				++b;
			}
		} else {
			if (a >= 1 && b >= 1) {
				++c;
				--a;
				--b;
			} else if (a >= 3) {
				a -= 3;
				++c;
			} else ok = false;
		}
	}

	if (ok) cout << "YES" << endl;
	else cout << "NO" << endl;

	return 0;
}
