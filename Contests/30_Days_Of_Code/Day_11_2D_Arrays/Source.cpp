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
#include <climits>
using namespace std;

#define N 6


int main(){
    vector< vector<int> > arr(N,vector<int>(N));
    for(int arr_i = 0;arr_i < N;arr_i++){
       for(int arr_j = 0;arr_j < N;arr_j++){
          cin >> arr[arr_i][arr_j];
       }
    }
    int res = INT_MIN;
    for (int i = 0; i < N; ++i)
    {
    	for (int j = 0; j < N; ++j)
    	{
    		if((i+2) < N && (j+2) < N)
    		res = max(res, 
    			arr[i][j] + arr[i][j+1] + arr[i][j+2]
    			+ arr[i+1][j+1]
    			+ arr[i + 2][j] + arr[i + 2][j+1] + arr[i + 2][j+2]);
    	}
    }
    cout << res << endl;

    return 0;
}
