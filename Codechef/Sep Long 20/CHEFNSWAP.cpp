// KUSHAGRA WADHWA 
#include<bits/stdc++.h>
using namespace std;
#define ll long long int


ll helper(ll num)
{
    long double a = sqrtl(1ul + 4 * (num));
    a = a - 1.0;
    a = a / 2.0;
    ll fin = a;
    return fin;
}

void solve()
{


    ll n;
    cin >> n;
    ll s = n * (n + 1) / 2;

    if(s % 2 != 0)
    {
        cout<<0;
        return;
    }



    ll x = helper(s);



    ll sub = x * (x + 1) / 2;

    if(s / 2 == sub)
    {
        ll kush = (x * (x - 1ul)) / 2l + ((n - x) * (n - x - 1ul)) / 2l + (n - x);
        cout << kush;
    }
    else
    {
        cout << n - x;
    }
    
}


int main() 
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    int testcase;
    cin >> testcase; 

    while(testcase--)
    {
        solve();
        cout << "\n";
    }
    return 0;
}