#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    string s;
    int c = 0;
    getline(cin, s);

    for(int i = 0; i < s.length(); i++) {
        if(s[i] == '(') ++c;
        else --c; 

        if(c < 0) {
            cout << i+1;
            break;
        }
    }

    return 0;
}