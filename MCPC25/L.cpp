#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> v(n);
        for (auto &i: v) {
            cin >> i;
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (v[i] > v[j]) {
                    swaps++;
                    swap(v[i], v[j]);
                }
            }
        }

        if (swaps % 2 == 0) {
            cout << swaps << endl;
        } else {
            cout << -1 << endl;
        }
    }
    
}
