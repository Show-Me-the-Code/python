/*	ZQU OJ 1360 快排 */
#include <iostream>
using std::cout;
using std::cin;
using std::endl;

const int MAX = 100000 + 2;
int n,A[MAX];
int bookl = 0,bookr = 0;
void print() {
    for(int i=0; i<n-1; i++)
        cout << A[i] << ' ';
    cout << A[n-1] << endl;
}
void QUICK(int left,int right) {
    //cout << c << " left = " << left << ' ' << "right = " << right << endl;
    if(left < right) {
        int pivot = A[left];
        int i = left,j = right;
        while(i < j) {
            while(j > i && A[j] >= pivot) {
                j--;
            }
            if(i < j)
            A[i++] = A[j];
            while(i < j && A[i] <= pivot) {
                i++;
            }
            if(i < j)
            A[j--] = A[i];
           // cout << "i = " << i << " j = " << j <<endl;
        }
        A[i] = pivot;
        print();
        QUICK(left,i-1);
        QUICK(i+1,right);
    }
   // else cout <<"Here" << endl;

}
int main()
{
    cin >> n;
	for(int i=0; i<n; i++)
		cin >> A[i];
    if(n == 1)
        cout << A[0] << endl;

	QUICK(0,n-1);/*
	for(int i=0; i<n; i++)
        cout << A[i] << ' ';
    cout << endl;
    */
	return 0;
}
