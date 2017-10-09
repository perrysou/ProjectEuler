/*
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <cmath>
#include <iostream>
#include <map>
using namespace std;

long collatz(long n, map<long, long> &chainDict){
    long n_new;
    auto it = chainDict.find(n);
    if (it == chainDict.end()){
        chainDict[n] = 1;
        if (n != 1){
            if (n % 2 == 0){
                n_new = n / 2;
            }
            else{
                n_new = n * 3 + 1;
            }
            chainDict[n] = collatz(n_new, chainDict) + 1;
        }
    }
    return chainDict[n];
}

int main(){
    int t;
    cin >> t;
//    t = rand() % int(pow(10, 4)) + 1;
//    t = 1;
    map<long, long> chainDict, chainMaxDict;
    long n, n_old = 0, chainMax = 0, k_old = 1;
    long step;
    while (t-- > 0){
        cin >> n;
//        n = rand() % long(5 * pow(10, 2)) + 1;
//        n = 10;
        if (n > n_old){
            step = -1;
        }
        else if (n < n_old){
            step = 1;
            chainMax = 0;
            k_old = 1;
        }
        else{
            cout << chainMaxDict[n] << endl;
            continue;
        }
        for (long nn = n; nn >= max(n_old, n / 2); nn += step){
            collatz(nn, chainDict);
        }
        for (auto k : chainDict){
            if (k.first <= n){
                if (k.second >= chainMax){
                    chainMax = k.second;
                    k_old = max(k.first, k_old);
                }
            }
        }
        chainMaxDict[n] = k_old;
        cout << k_old << endl;
        n_old = n;
    }
}
