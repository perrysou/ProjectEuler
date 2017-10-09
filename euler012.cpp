//
// Created by Yang Su on 9/15/17.
//

#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <cstdlib>
#include <numeric>
#include <iostream>
using namespace std;

std::vector<int> sieveofEratosthenes(int n){
    std::vector<int> nums(n - 1);
    std::iota(nums.begin(), nums.end(), 2);
    for (int i = 2; i <= int(sqrt(n)); ++i){
        if (nums[i - 2] != 0){
            for (int j = i - 2 + i; j <= n - 2; j += i){
                nums[j] = 0;
            }
        }
    }
    auto pend = std::remove_if(nums.begin(), nums.end(), [](int x){return (x == 0);});
    std::vector<int> nums_new(nums.begin(), pend);
    return nums_new;
}

tuple<int, vector<int>> getPrimeFactors(int n, vector<int> primeSet) {
    map<int, int> primeCount;
    int total = 1;

    for (auto x: primeSet) {
        int temp = 0;
        while (n % x == 0) {
            temp += 1;
            n /= x;
        }
        if (temp != 0) {
            total *= (temp + 1);
            primeCount[x] = temp;
        }
        if (n == 1) {
            break;
        }
    }
    if (n != 1) {
        total *= 2;
        primeCount[n] = 1;
        primeSet.push_back(n);
    }
    return {total, primeSet};
}
vector<int> genTriangleNumberSequence(int n) {
    vector<int> tri;
    int total = 0;
    for (int i = 1; i <= n; i++){
        total += i;
        tri.push_back(total);
    }
    return tri;
}

int genTriangleNumber(int n) {
    return n * (n + 1) / 2;
}

int euler012(int argc, const char * argv[]) {
    vector<int> primeSet = sieveofEratosthenes(1000);
    map<int, int> divisorDict;
    int t, n;
    cin >> t;
    while (t-- > 0){
        cin >> n;
        int diff = n;
        int tri = genTriangleNumber(n);
        while (true){
            int nd;
            tie(nd, primeSet) = getPrimeFactors(tri, primeSet);
            auto it = divisorDict.find(nd);
            if (it == divisorDict.end()){
                divisorDict[nd] = tri;
            }
            else{
                divisorDict[nd] = min(tri, divisorDict[nd]);
            }
            if (nd > n){
                cout << tri << endl;
                break;
            }
            diff++;
            tri += diff;
        }
    }
}