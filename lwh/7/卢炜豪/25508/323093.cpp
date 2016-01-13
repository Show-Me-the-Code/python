#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;
int main()
{
	long long int  N,T,A[100005],ans=1;
	scanf("%lld %lld",&N,&T);
	for(int i = 1; i<=N ; i++)
        A[i] = 0;
	for(int i=1 ; i<=N ; i++){
		long long int l,s;
		scanf("%lld %lld",&l,&s);
		A[i] = l + s * T;
	}
	long long int temp = A[N];

	for(int i=N; i > 0 ; i--){
		if(A[i] < temp){
			ans ++;
			temp = min(A[i],temp);
		}
	}
	printf("%lld\n",ans);
}
