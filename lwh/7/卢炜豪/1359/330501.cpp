/* ZQU OJ 1359 */
#include <iostream>
using namespace std;
const int MAX = 100000+5;
int main()
{
	int n,A[MAX],k,i;
	bool EX = true;

	cin >> n;
	k = n;

	for(int i=0; i<n; i++)
        cin >> A[i];

    while(EX) {
        EX = false;
        for(i=1; i<n; i++) {
            if(A[i-1] > A[i]) {
                int tmp = A[i];
                A[i] = A[i-1];
                A[i-1] = tmp;
               // n = i;
                EX = true;
            }
          //  cout << i << endl;
        }
        n = i;
        for(int j=0; j<k; j++)
            cout << A[j] << ' ';
        cout << endl;
    }
}
