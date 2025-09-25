#include <iostream>
using namespace std;

int main(void)
{
    int t;
    cin >> t;
    while (t--)
    {
        long long y;
        cin >> y;
        if (y % 5 == 0 && y % 10 != 0)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}
