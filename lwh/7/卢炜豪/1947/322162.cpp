#include <cstdio>
#include <cstring>
#include <algorithm>

#define Max 10000 + 5

using namespace std;

int main()
{
	int n;
	while(scanf("%d",&n) != EOF)
	{
		int A[Max],Sum = 0,sum[Max];

		memset(sum,0,sizeof(sum[0]));

		for(int i = 0;i < n;i++)
			scanf("%d",&A[i]);

		sum[0] = A[0];Sum = 0;
		for(int i = 1; i < n;i++)
		{
			sum[i] = max(sum[i-1] + A[i],A[i]);
			if(sum[i] > Sum)
                Sum = sum[i];
			//printf("sum[%d]=%d A[%d]=%d\n",i,sum[i],i,A[i]);
		}
		printf("%d\n",Sum);
	}
}
