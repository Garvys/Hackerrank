#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    float M,T,X;
    cin >> M >> T >> X;
    float tip = (float)(T*M) / (float)(100);
    float tax = (float)(X*M) / (float)(100);
    float result = tip + tax + (float)M;
    cout << "The final price of the meal is $" << (int)floor(result + 0.5) << "." << endl;
    return 0;
}