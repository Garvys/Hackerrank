#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;


int main() {
    int N;
    cin >> N;
    vector<int> arr;
    for(int i  = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    sort(arr.begin(),arr.end());
    int min_diff = INT_MAX;
    vector<int> i_min;
    for(int i = 0; i < (N-1); i++)
    {
        if((arr[i+1] - arr[i]) < min_diff)
        {
            min_diff = arr[i+1] - arr[i];
            i_min.clear();
            i_min.push_back(i);
            continue;
        }
        if((arr[i+1] - arr[i]) == min_diff)
        {
            i_min.push_back(i);
        }
    }
    for(int i = 0; i < (int)i_min.size(); i++)
        cout << arr[i_min[i]] << " " << arr[i_min[i]+1] << " ";
    return 0;
}
