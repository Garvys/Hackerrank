#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void ConvertToBinary(int n)
{
    if (n / 2 != 0) {
        ConvertToBinary(n / 2);
    }
    //printf("%d", n % 2);
    cout << n % 2 ;
}

int main() {
   	int T = 0;
   	cin >> T;
   	for (int t = 0; t < T; ++t)
   	{
   		int32_t n = 0;
   		cin >> n;
   		ConvertToBinary(n);
   		cout << endl;
   	}
    return 0;
}
