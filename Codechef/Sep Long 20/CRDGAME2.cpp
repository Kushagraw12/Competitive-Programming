// KUSHAGRA WADHWA
#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define MOD 1000000007

ll helper(ll a, ll n) 
{ 
    ll kush = 1; 
    while (n) { 
        if (n & 1) 
            kush = kush * a % MOD; 
        n = n / 2; 
        a = a * a % MOD; 
    } 
    return kush; 
} 

ll min(ll a,ll b)
{
    return (a < b ? a : b);
}


ll d(ll a,ll b)
{
    return (a % MOD * (helper(b, MOD - 2) % MOD)) % MOD;
}


ll sol(ll n, ll r)
{
    ll ans = 1;
    ll k = min(r, n - r);
    
    for(int i = 0; i<k; i++){
        ans = (ans % MOD * (n - i) % MOD) % MOD;
        ans = d(ans, i + 1);
    }
    
    return (ans % MOD);
}


int solve()
{
    int n;
    cin>>n;
    
    ll k[n], ans;

    for(int i = 0; i < n; i++)
    {
        cin>>k[i];
    }

    ll m = 0, val = 0;
    
   for(int i = 0; i < n; i++){
        if(m < k[i])
            m = k[i];
   }


    for(int i = 0; i < n; i++){
        if(m == k[i])
            val++;
    }

    if(n == 1){
        return 2;
    }


    if(val % 2 != 0)
        ans = helper(2, n) % MOD;

    else
    {
        ans = helper(2, n) % MOD - ((helper(2, n - val) % MOD) * sol(val, val / 2) % MOD) % MOD;
    }

    if(ans < 0)
        ans = (ans + MOD) % MOD;

    return (ans % MOD);
}

int main() 
{
 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int test;
    cin>>test;
    
    while(test--)
    {
        cout << solve() << endl;
    }
    return 0;
   
}