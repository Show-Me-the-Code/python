#include <cstdio>
int main()
{
	int N,K,cow[50005];
	scanf("%d %d",&N,&K);

	for(int i = 0;i < N;i++)
		scanf("%d",&cow[i]);

	int ans=-1,tmp=-1;

	for(int i = 0;i < N;i++)
	{
		for(int j = i;j < N;j++)
		{
			if(cow[i]==cow[j] && i!=j && j <= i + K)
			{
				tmp = cow[i];
				//printf("i=%d j=%d tmp=%d\n",i,j,tmp);
			}
		}
		if(ans < tmp)
			ans = tmp;

	}

	printf("%d\n",ans);
}
