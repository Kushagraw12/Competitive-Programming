#include <bits/stdc++.h>
using namespace std;
#define INF 1e9

int main()
{
    int total;
    cin >> total;
    while (total--)
    {
        int n, k, m;
        cin >> n >> k >> m;
        int counter = 1;
        vector<int> a(m);
        for (auto &it : a)
            cin >> it;
        int p = a[0] / k + 1;
        for (int i = 1; i < m; ++i)
        {
            if (a[i] / k + 1 == p)
            {
                continue;
            }
            p = a[i] / k + 1;
            counter++;
        }
        cout << counter << endl;
    }
    return 0;
}