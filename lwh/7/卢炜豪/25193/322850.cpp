#include <cstdio>
#include <math.h>
const int Max=100000+5;
int main()
{
	int N;
	int A[Max];
	long long int ans = 0;

	scanf("%d",&N);

	for(int i=1;i<=N;i++)
		scanf("%d",&A[i]);

	A[0]=A[N+1]=0;

	for(int i = 1;i <= N;i++)
	{
		if(A[i] > A[i-1])
			ans += abs(A[i]-A[i-1]);
	}
	printf("%lld\n",ans);
}
