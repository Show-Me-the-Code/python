/* ZQU OJ 1357 直接插入排序 */
#include <stdio.h>
const int MAX = 100000 + 2;
int main()
{


	int n,A[MAX]; //n个整数
	scanf("%d",&n);

	for(int i=0; i<n; i++)
		scanf("%d",&A[i]);

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
            printf("%d ",A[k]);
            printf("%d\n",A[n-1]);
        //cout << endl;
    }
}
