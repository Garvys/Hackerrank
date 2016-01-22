#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>
using namespace std;

std::vector<std::string> resplit(const std::string & s, std::string rgx_str = "\\s+") 
{
    std::vector<std::string> elems;
    std::regex rgx (rgx_str);
    std::sregex_token_iterator iter(s.begin(), s.end(), rgx, -1);
    std::sregex_token_iterator end;
    while (iter != end)
    {
        //On ne prend ps les éléments vide notament ee premier
        if((*iter).length() > 0)
            elems.push_back(*iter);
        ++iter;
    }
    return elems;
}

int main() {
    string s;
    getline(cin,s);
    vector<string> v = resplit(s,"[\\W\\_]+");
    cout << v.size()<< endl;
    for(int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
    return 0;
}
