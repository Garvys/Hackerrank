#include <cassert>
#include <iostream>
#include <algorithm>

using namespace std;

int a, b, c, d, res;

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin >> a >> b >> c >> d;
    for(int i = 1; i <= a; i++)
        for(int j = 1; j <= b; j++)
            for(int k = 1; k <= c; k++)
                for(int l = 1; l <= d; l++)
                    if ((abs(i - j) % 3 == 0) && ((j + k) % 5 == 0) && (i * k % 4 == 0) && (__gcd(i, l) == 1))
                        ++res;
    cout << res << endl;
    return 0;
}