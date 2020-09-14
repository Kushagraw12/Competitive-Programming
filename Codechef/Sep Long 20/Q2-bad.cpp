#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll helper(ll num){
    return (num * (num + 1)) / 2;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int testcase;
    cin>>testcase;
    while(testcase--)
    {
        
        int n;
        cin >> n;
        ll sum = (n * (n + 1)) / 2;
        ll ans = 0;
        if(sum & 1){ 
            ans = 0;
        }
        else{
            double tempo = sum / 2;
            double k = (sqrt( 8 * tempo + 1) / 2) - 0.5;
            
            double d, i;
            
            d = modf(k, &i);
            ll a = (ll)k;
            
            if(d == 0){
                ans = helper(a - 1) + helper(n - a - 1);
            }
            ans += n - a;
        }
        cout << ans << endl;
    }
} 