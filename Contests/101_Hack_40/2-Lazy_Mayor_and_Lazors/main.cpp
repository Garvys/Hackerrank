#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main() {
	long long int n = -1;
	cin >> n;
	vector<long long int> h(n);
	for (long long int i = 0; i < n; i++)
		cin >> h[i];
	long long int m = -1;
	cin >> m;
	vector<long long int> x_l(m);
	for (long long int i = 0; i < m; i++)
		cin >> x_l[i];
	sort(x_l.begin(), x_l.end());
	long long int imin = 0;
	for(long long int j = 0; j < m; j++) {
		long long int x = x_l[j];
		bool nothingRemoved = true;
		for(long long int i = imin; i < (x-1); i++) {
			if (h[i] > (x-(i+1))) {
				if (nothingRemoved)
					imin = i+1;
				nothingRemoved = false;
				h[i] = x-(i+1);
			}
		}
	}
	long long int res  = 0;
	for(long long int i = 0; i < n; i++) {
		res += h[i];
	}
	cout << res << endl;
	return 0;
}

