#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    map<string,string> my_map;
    int n;
    cin >> n;
    cin.ignore();
    for(int i = 0; i < n; i++)
    {
        string name, num;
        getline(cin,name);
        getline(cin,num);
        cerr << name << " - " << num << endl;
        my_map[name] = num;
    }
    while(1)
    {
        string in;
        getline(cin,in);
        if(in.empty())
            break;
        cerr << in << endl;
        if(my_map.count(in) > 0)
            cout << in << "=" << my_map[in] << endl;
        else
            cout << "Not found" << endl;
    }
    return 0;
}
