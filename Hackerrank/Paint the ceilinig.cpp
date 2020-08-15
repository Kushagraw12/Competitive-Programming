#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll variantsCount(ll n,ll s0,ll k,ll b,ll m,ll a)
{
   ll s[n];
   ll i,j;
   s[0]=s0;
   for(i=1;i<n;i++) // finding the value of s and store it in the array
   {
       s[i] = ((k%m*s[i-1]%m)%m+b)%m + 1 + s[i-1];
   }
   ll ans=0;
   i=0;
   j=n-1;
   while(i<j) // using two pointer technique
   {
       if((s[i]*s[j]) <= a) // whenever we found a pair it means it will hold all (i,k) where k is in the range [i+1,j]
       {
           ans += (j-i); // hence there will be (j-i) pairs. (i,i) pair is also valid but i am not counting it here
           i++; // when we found a pair then we increase the first pointer
       }
       else
       {
           j--; // otherwise we decrease last pointer to get smaller product
       }
   }
   ans = ans * 2; // if (i,j) is valid pair then (j,i) will also be valid pair. so,multiplied by 2.
   for(i=0;i<n;i++)
   {
       if((s[i]*s[i]) <= a) // if product with itself satisfies then count will be increased by 1.
           ans++;
   }
   return ans;
}
int main()
{
   ll n,s0,k,b,m,a;
   cin>>n;
   cin>>s0;
   cin>>k>>b>>m;
   cin>>a;
   ll ans;
   ans = variantsCount(n,s0,k,b,m,a);
   cout<<ans;
   return 0;
}