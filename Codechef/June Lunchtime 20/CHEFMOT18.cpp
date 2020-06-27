#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int32_t main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int s, n;
        cin >> s >> n;
        int ans = 0;
        if (s <= n)
        {
            if (s % 2 && s > 1)
            {
                ans += 2;
            }
            else
            {
                ans += 1
            };
        }
        else if (n % 2)
        {
            int x = s / (n - 1);
            ans += x;
            if (s % (n - 1) != 0)
            {
                if ((s % (n - 1)) % 2 && (s % (n - 1)) > 1)
                {
                    ans += 2;
                }
                else
                {
                    ans += 1
                };
            }
        }
        else
        {
            int x = s / n;
            ans += x;
            if (s % n != 0)
            {
                if ((s % n) % 2 && (s % n) > 1)
                {
                    ans += 2;
                }
                else
                {
                    ans += 1
                };
            }
        }
        cout << ans << endl;
    }
}