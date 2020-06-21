#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF 1e9

int32_t main()
{
    int total;
    cin >> total;
    while (total--)
    {
        int n, m;
        cin >> n >> m;
        set<int> stroll;
        map<int, int> kush;
        for (int i = 0; i < n; ++i)
        {
            int te;
            cin >> te;
            stroll.insert(te);
            kush[te]++;
        }
        int count = 0;
        for (int j = 1; j < m; ++j)
        {
            if (*stroll.lower_bound(j) == j)
            {
                count += kush[j];
            }
            else
            {
                count = 0;
                break;
            }
        }
        if (count == 0)
        {
            cout << -1 << endl;
        }
        else
        {
            for (auto i = stroll.upper_bound(m); i != stroll.end(); i++)
            {
                count += kush[*i];
            }
            cout << count << endl;
        }
    }
    return 0;
}
