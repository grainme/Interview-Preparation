#include <iostream>
using namespace std;

int main(void) {
    int t;
    cin >> t;
    while (t--)
    {
        int a, b, x;
        cin >> a >> b >> x;
        int ropes = (b / x);
        int shirts = b % x;

        long long mx = ropes * (min(b,x) + 1) + (shirts > 0 ? shirts + 1 : 0);
        if (mx > a)
        {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
        
    }
    
}
