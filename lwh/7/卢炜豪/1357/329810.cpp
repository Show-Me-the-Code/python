/* ZQU OJ 1357 直接插入排序 */
#include <iostream>
const int MAX = 100000 + 2;
using namespace std;
int main()
{

	cout.sync_with_stdio(false);

	int n,A[MAX]; //n个整数
	cin >> n;

	for(int i=0; i<n; i++)
		cin >> A[i];

    for(int i=1; i<n; i++) {
        int t = i;
        for(int j=i-1; j>=0; j--) {
            if(A[t] > A[j]) {
                int temp = A[t];
                A[t] = A[j];
                A[j] = temp;
                t = j;
            }
        }
        for(int k=0; k<n-1; k++)
            cout << A[k] << ' ';
            cout << A[n-1];
        cout << endl;
    }
}
