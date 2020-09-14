// KUSHAGRA WADHWA
#include<bits/stdc++.h>
using namespace std;
#define ll long long int



int helper()
{
    ll n, ans=0;

    cin >> n;


    vector<ll> val;

    ll x;

    for(int i = 1; i <= 20; i++){
        cout << 1 << " " << (1ul << i) << endl;
        cout.flush();
        cin >> x;
        val.push_back(x);
    }


    reverse(val.begin(), val.end());


    ll s = val[0] - n * (1ul << 20);

    for(int i = 1; i < val.size(); i++){
        if(val[i] >= s){
            val[i] = ((n - (val[i] - s) / (1ul << (val.size() - i))) / 2);
        }
        else{
            val[i] = (n + (s - val[i]) / (1ul << (val.size() - i))) / 2;
        }
    }


    for(int j = 1; j < val.size(); j++){
        if(val[j] % 2 != 0)
            ans += 1ul << (val.size() - j);
    }

    if(s % 2 != 0)
        ans++;

    cout << 2<< " " << ans << endl;
    cout.flush();

    int kush;
    cin >> kush;
    return kush;
} 
 
int main() 
{
 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int testcase;
    cin>>testcase;
    
    while(testcase--)
    {
        if(!helper())
            break;
        
        cout << endl;
        cout.flush();
    }
    return 0;
}