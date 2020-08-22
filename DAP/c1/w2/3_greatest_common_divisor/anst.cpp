#include <iostream>
//#include<bits/c++>


int solve(int a, int b){
	if(b == 0){
		return a;
	}
	solve(b, a%b);
}

int main() {
	int a, b, ans;
	std::cin >> a>> b;
	ans = solve(a,b);
	std::cout << ans;
}

