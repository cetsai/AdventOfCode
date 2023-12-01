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
/*
// : All variables are unsigned 32 bit and wrap modulo 2^32 when calculating
var int s[64], K[64]
var int i

// Notice: the two padding steps above are implemented in a simpler way
//  in implementations that only work with complete 1bytes: append 0x80
//  and pad with 0x00 bytes so that the message length in bytes ≡ 56 (mod 64).

append original length in bits mod 264 to message

// Process the message in successive 512-bit chunks:
for each 512-bit chunk of padded message do
    break chunk into sixteen 32-bit words M[j], 0 ≤ j ≤ 15
    // Initialize hash value for this chunk:
    var int A := a0
    var int B := b0
    var int C := c0
    var int D := d0
    // Main loop:
    for i from 0 to 63 do
        var int F, g
        if 0 ≤ i ≤ 15 then
            F := (B and C) or ((not B) and D)
            g := i
        else if 16 ≤ i ≤ 31 then
            F := (D and B) or ((not D) and C)
            g := (5×i + 1) mod 16
        else if 32 ≤ i ≤ 47 then
            F := B xor C xor D
            g := (3×i + 5) mod 16
        else if 48 ≤ i ≤ 63 then
            F := C xor (B or (not D))
            g := (7×i) mod 16
        // Be wary of the below definitions of a,b,c,d
        F := F + A + K[i] + M[g]  // M[g] must be a 32-bits block
        A := D
        D := C
        C := B
        B := B + leftrotate(F, s[i])
    end for
    // Add this chunk's hash to result so far:
    a0 := a0 + A
    b0 := b0 + B
    c0 := c0 + C
    d0 := d0 + D
end for

var char digest[16] := a0 append b0 append c0 append d0 // (Output is in little-endian)
*/

inline uint32_t rotate_left(uint32_t x, int n) {
    return (x << n) | (x >> (32-n));
}

uint32_t md5(string message) {
    uint32_t k[64] =
        {0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391};

    int32_t s[64] = {   7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
                        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
                        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
                        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 };

    uint32_t a0 = 0x67452301;   // A
    uint32_t b0 = 0xefcdab89;   // B
    uint32_t c0 = 0x98badcfe;   // C
    uint32_t d0 = 0x10325476;   // D

    // pad message
    uint8_t m[64];
    for(int i = 0; i < message.length(); ++i){
        m[i] = message[i];
    }
    m[message.length()] = 0x08;
    for(int i = message.length() + 1; i < 56; ++i){
        m[i] = 0;
    }
    uint64_t len = message.length();
    ((uint64_t*) m)[7] = len;

    uint32_t* chunk = ((uint32_t*) m);
    
    for (int i = 0; i < 16; ++i) {
        
        uint32_t a = a0;
        uint32_t b = b0;
        uint32_t c = c0;
        uint32_t d = d0;

        for (int j = 0; j < 64; ++j) {
            uint32_t f, g;
            if (j <= 15) {
                f = (b & c) | ((!b) & d);
                g = j;
            } else if (j <= 31) {
                f = (d & b) | ((!d) & c);
                g = (5 * j + 1) % 16;
            } else if (j <= 47) {
                f = b ^ c ^ d;
                g = (3 * j + 5) % 16;
            } else {
                f = c ^ (b | (!d));
                g = (7 * j) % 16;
            }
            f = f + a + k[i] + chunk[g];  // M[g] must be a 32-bits block
            a = d;
            d = c;
            c = b;
            b = b + rotate_left(f, s[i]);
        }
        a0 += a;
        b0 += b;
        c0 += c;
        d0 += d;
    }

    return a0;

}

void partOne() {
    unsigned int count = 0;
    do {
        string s ("bgvyzdsv");
        s.append(std::to_string(count));
        uint32_t out = md5(s);
        if (count < 10) {
            cout << s << " " << hex << out << dec << endl;
        }
        if (out <= 0x00000fff) {
            cout << dec << count << " " << hex << out << endl;
            cout << "finished" << endl;
            break;
        }
        ++count;
    }while(true);
    cout << dec << count;
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    partOne();

    return 0;
}