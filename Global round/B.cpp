#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;
int k;
string ans;
void solve(string &a, int k)
{
    string temp;
    if (k == 1)
    {
        ans = a;
    }
    else
    {
        string temp;
        for (int i = 0; i < k - 1; i++)
        {
            temp += 's';
        }
        ans += temp;
    }
}

int main()
{
    ll k;
    cin >> k;
    string a = "codeforces";
    solve(a, k);
    cout << ans << endl;

    return 0;
}