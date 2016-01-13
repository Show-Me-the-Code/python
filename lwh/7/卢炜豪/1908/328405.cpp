#include <iostream>
using namespace std;
int A(int n,int m) {
	int ret;
	if(n == 1 && m == 0) {
		ret = 2;
		return ret;
	}
	else if(n == 0) {
		ret = 1;
		return ret;
	}
	else if(n >=2 && m == 0) {
		ret = n + 2;
		return ret;
	}
	else {
		A(A(n-1,m),m-1);
	}
	//return ret;
}
int main()
{
	int n,m;
	while(cin >> n >> m) {
		cout << A(n,m) << endl;
	}
	return 0;
}
