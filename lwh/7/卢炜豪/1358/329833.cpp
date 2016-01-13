/* ZQU OJ 135 shell排序 */
#include <iostream>
const int MAXN = 100000 + 2;
const int MAXB = 20 + 2;
int main()
{
	using std::cout;using std::cin;
	using std::endl;
	cout.sync_with_stdio(false);
	int n,a;		//n表示整数个数，a表示步长个数
	int A[MAXN],B[MAXB];		//A存待排数，B存步长数
	cin >> n >> a;

	for(int i=0; i<a; i++)
		cin >> B[i];
	for(int i=0; i<n; i++)
		cin >> A[i];

	for(int i=0; i<a; i++) {
		int step = B[i];
		for(int j=step; j<n; j++) {
            int t=j;
			for(int k=j-step; k>=0; k-=step) {
                if(A[t] < A[k]) {
                    int temp = A[t];
                    A[t] = A[k];
                    A[k] = temp;
                    t = k;
                }
                else break;
			}
		}
		for(int y=0; y<n-1; y++)
			cout << A[y] << ' ';
			cout << A[n-1] << endl;
	}
}
