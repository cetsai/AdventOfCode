#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>
#include <cstdio>

using namespace std;

void partOne() {
    int sum = 0;
    string s,t;
    while(getline(cin,s)) {
        int dims[3];
        stringstream ss (s);
        for(int i = 0; i < 3; i++){
            getline(ss, t, 'x');
            dims[i] = atoi(t.c_str());
        }
        int a = 2*dims[0]*dims[1];
        int b = 2*dims[0]*dims[2];
        int c = 2*dims[1]*dims[2];
        int d;
        if (a <= b && a <= c)  d = a / 2;
        else if (b <= a && b <= c) d = b / 2;
        else d = c / 2;
        cout << dims[0] << " " << dims[1] << " " << dims[2] << " | " << a << " " << b << " " << c << " " << d << " : " << a + b + c  << endl; 
        sum += a + b + c + d;
    }

    cout << sum;
}

void partTwo() {
    int sum = 0;
    string s,t;
    while(getline(cin,s)) {
        int dims[3];
        stringstream ss (s);
        for(int i = 0; i < 3; i++){
            getline(ss, t, 'x');
            dims[i] = atoi(t.c_str());
        }
        int vol = dims[0] * dims[1] * dims[2];
        int p;
        if (dims[0] >=dims[1] && dims[0] >= dims[2]) p = 2 * dims[1] + 2 * dims[2];
        else if (dims[1] >= dims[0] && dims[1] >=dims[2]) p = 2 * dims[0] + 2 * dims[2];
        else p = 2 * dims[0] + 2 * dims[1];
        cout << p << " " << vol << " " << p + vol << endl;
        sum += p + vol;
    }
    cout << sum;
}
 
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    partTwo();
    
 
    return 0;
}