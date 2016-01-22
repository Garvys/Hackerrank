#include <iostream>
#include <vector>

using namespace std;

template <class T>
void printArray(vector<T> v)
{
    for(int i = 0; i < (int)v.size();i++)
        cout << v[i] << endl;
}

int main()
{
    vector<int> vInt{1, 2, 3};
    vector<string> vString{"Hello", "World"};
    
    printArray<int>(vInt);
    printArray<string>(vString);
    
    return 0;
}