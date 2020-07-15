#include <bits/stdc++.h>
using namespace std;

#define mod 1e9 + 7
typedef long long int ll;
#define fori(i, n) for (ll(i) = 0; (i) < (n); (i)++)
#define foria(i, a, b) for (ll(i) = (a); (i) <= (b); (i)++)
#define foriar(i, a, b) for (ll(i) = (a); (i) >= (b); (i)--)
#define ff first
#define ss second
#define pb push_back
#define pob pop_back

ll power(ll b, ll p)
{
    ll res = 1;
    while (p--)
        res = res * b;
    return res;
}
ll binaryToDecimal(string n)
{
    string num = n;
    ll dec_value = 0;

    ll base = 1;

    ll len = num.length();
    for (ll i = len - 1; i >= 0; i--)
    {
        if (num[i] == '1')
            dec_value += base;
        base = base * 2;
    }

    return dec_value;
}

void sol()
{
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n), f(31, 0);
    vector<pair<ll, ll>> val(31);
    fori(i, n)
    {
        cin >> a[i];
    }
    fori(i, 31)
    {
        ll bit = power(2, i);
        fori(j, n)
        {
            if (a[j] & bit)
                f[i]++;
        }
        val[i].ff = f[i] * bit;
        val[i].ss = i;
    }
    sort(val.begin(), val.end());
    ll ans = 0, j;
    for (ll i = 30; i >= 0 && k;)
    {
        j = i;
        while (val[j].ff == val[i].ff && j >= 0)
            j--;
        j++;
        ll r = i - j + 1;
        if (r >= k)
        {
            foria(w, j, j + k - 1)
                ans += power(2, val[w].ss);
            k = 0;
        }
        else
        {
            foria(w, j, i)
                ans += power(2, val[w].ss);
            k -= r;
            i = j - 1;
        }
    }
    cout << ans << endl;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll total = 1;
    cin >> total;
    for (ll _ = 0; _ < total; _++)
    {
        sol();
    }
    return 0;
}