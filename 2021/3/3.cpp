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
#include <utility>

using namespace std;
using coords = pair<int,int>;

struct pair_hash
{
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2> &pair) const {
        return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
    }
};


void partOne() {
    coords loc(0,0);
    unordered_set<coords, pair_hash> visited;
    visited.insert(loc);
    char c;
    while(cin.get(c)){
        if (c == '^') {
            loc = make_pair<int, int>(loc.first + 0, loc.second + 1);
            visited.insert(loc);
        }
        else if (c == '>') {
            loc = make_pair<int, int>(loc.first + 1, loc.second + 0);
            visited.insert(loc);
        }
        else if (c == 'v') {
            loc = make_pair<int, int>(loc.first + 0, loc.second - 1);
            visited.insert(loc);
        } 
        else {
            loc = make_pair<int, int>(loc.first - 1, loc.second + 0);
            visited.insert(loc);
        }
    }

    cout << visited.size();
}

void partTwo() {
    coords loc1(0,0);
    coords loc2(0,0);
    bool santa = true;
    unordered_set<coords, pair_hash> visited;
    visited.insert(loc1);
    char c;
    while(cin.get(c)){
        coords& loc = santa ? loc1 : loc2;
        if (c == '^') {
            loc = make_pair<int, int>(loc.first + 0, loc.second + 1);
            visited.insert(loc);
        }
        else if (c == '>') {
            loc = make_pair<int, int>(loc.first + 1, loc.second + 0);
            visited.insert(loc);
        }
        else if (c == 'v') {
            loc = make_pair<int, int>(loc.first + 0, loc.second - 1);
            visited.insert(loc);
        } 
        else {
            loc = make_pair<int, int>(loc.first - 1, loc.second + 0);
            visited.insert(loc);
        }
        santa = !santa;
    }

    cout << visited.size();
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    partTwo();

    return 0;
}
