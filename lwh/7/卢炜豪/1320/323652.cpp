#include <cstdio>
#include <cstring>
const int Maxn = 10000+5;
int A[Maxn][Maxn];
int B[Maxn][Maxn];
int C[Maxn][Maxn];
int book[Maxn][Maxn];
int main()
{
	int m,n,c,k=0;
	scanf("%d %d %d",&m,&n,&c);
	k=c;
	int e,f,v;
	for(int i=0 ; i<c ; i++) {
		scanf("%d %d %d",&e,&f,&v);
		A[e][f]=v;
		book[e][f]=1;
	}
	scanf("%d %d %d",&m,&n,&c);
	k+=c;
	for(int i=0 ; i<c ; i++) {
		scanf("%d %d %d",&e,&f,&v);
		B[e][f]=v;
		book[e][f]=1;
	}
	printf("%d %d %d\n",m,n,k);
	for(int i=0 ; i<m ; i++) {
		for(int j=0 ; j<n ; j++) {
			if(book[i][j]!=0) {
				C[i][j]=A[i][j]+B[i][j];
				printf("%d %d %d\n",i,j,C[i][j]);
			}
		}
	}
}
