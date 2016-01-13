#include <iostream>
#include <cmath>
const int MAX = 100000 + 5;
int main()
{
	using std::cout;
	using std::cin;
	using std::endl;
	using std::min;

	int n,A[MAX],MIN,tmp,j=0;

	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> A[i];
		if(i != 0) {
			MIN = min(A[i],A[i-1]);
		}
	}

	for(int i=0; i<n-1 ;i++) {
		MIN = A[i];
		tmp = i;
		//cout << "A[i]= "<< A[i] << ' ';
		for(j=i; j<n; j++) {
			if(A[j] < MIN) {
				MIN = A[j];
				tmp = j;
			}
		}
		//cout << "MIN=" << MIN << ' ' << "tmp=" << tmp << ' ' << endl;
		int temp = A[i];
		A[i] = MIN;
		A[tmp] = temp;
		for(int k=0; k<n-1; k++)
			cout << A[k] << ' ';
		cout << A[n-1] << endl;
	}


}
