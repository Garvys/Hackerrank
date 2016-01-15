#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        int a, b ,N;
        cin >> a >> b >> N;
        int result = a;
        for(int n = 0; n < N ; n++)
        {
            result += b*(1 << n);
            cout << result << " ";
        }
        cout << endl;
    }
    return 0;
}