/*	ZQU OJ 1360 快排 */
#include <iostream>
using std::cout;
using std::cin;
using std::endl;

const int MAX = 100000 + 2;
int n,A[MAX];
int bookl = 0,bookr = 0;
void QUICK(int left,int right) {
 //   cout << "left = " << left << ' ' << "right = " << right << endl;
    if(left < right) {
        int pivot = A[left];
        int i = left,j = right;
        while(i < j) {
            while(j > i && A[j] >= pivot) {
                j--;
            }
            if(i < j)
            A[i++] = A[j];
            while(i < j && A[i] < pivot) {
                i++;
            }
            if(i < j)
            A[j--] = A[i];
        //    cout << "i = " << i << " j = " << j <<endl;
        }
        A[i] = pivot;
        QUICK(left,i-1);
        QUICK(j+1,n-1);
    }
    else {
        if(left >= right) {
            for(int k=0; k<n; k++)
                cout << A[k] << ' ';
            cout << endl;
        }
    return;
    }

}
int main()
{
    cin >> n;
	for(int i=0; i<n; i++)
		cin >> A[i];

	QUICK(0,n-1);
	return 0;
}
