// AUTHOR: KUSHAGRA WADHWA
#include <bits/stdc++.h>
#include <climits>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++)
    {
        cout << "Case #" << test << ": ";
        int N;
        cin >> N;
        vector<pair<int, int>> tree(N);
        for (int i = 0; i < N; i++)
        {
            cin >> tree[i].first;
            cin >> tree[i].second;
        }
        sort(tree.begin(), tree.end());

        map<int, int> uptop, downlow;

        for (int i = 0; i < N; i++)
        {
            int st = tree[i].first;
            int stop = tree[i].first + tree[i].second;
            uptop[stop] = max(uptop[stop], uptop[st] + tree[i].second);
        }

        for (int i = N - 1; i >= 0; i--)
        {
            int st = tree[i].first;
            int stop = tree[i].first - tree[i].second;
            downlow[stop] = max(downlow[stop], downlow[st] + tree[i].second);
        }

        int ans = 0;

        for (auto current : uptop)
        {
            int position = current.first;
            ans = max(ans, uptop[position] + downlow[position]);
        }
        for (auto current : downlow)
        {
            int position = current.first;
            ans = max(ans, uptop[position] + downlow[position]);
        }

        cout << ans << endl;
    }
}