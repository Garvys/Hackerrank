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

	int n,m;
	cin >> n >> m;
	vector<pair<int,int>> edges(m);
	vector<int> father(m+1,-1);
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		edges[i] = make_pair(a,b);
		father[b] = a;
	}
	vector<int> top_order(n);
	for(int i = 0; i < n; i++) {
		cin >> top_order[i];
	}

	vector<int> new_top_order(n,-1);
	vector<bool> isIn(m+1,false);
	for(int i = 0; i < n; i++) {
		int val = 1;
		if (i == 0) 
			val = top_order[0];
		while(true) {
			if(val <= n && !isIn[val]) {
				if (father[val] == -1 || isIn[father[val]]) {
					isIn[val] = true;
					new_top_order[i] = val;
					break;
				}
			}
			val++;
		}
		if (new_top_order[i] == -1) {
			new_top_order[i] = top_order[i];
			isIn[top_order[i]] = true;
		}
	}

	for(int i = 0; i < n; i++) {
		cout << new_top_order[i] << " ";
	}
	cout << endl;

	return 0;
}