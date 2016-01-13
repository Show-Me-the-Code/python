#include <cstdio>
int main()
{
	int N,K,cow[50005];
	scanf("%d %d",&N,&K);
	for(int i = 1;i <= N;i++)
		scanf("%d",&cow[i]);

	int ans = -1,temp = -1;
	for(int i = 1;i <= N;i++)
	{
		for(int j = i;j <= i+K && j <= N;j++)
		{
			if(cow[i]==cow[j] && i!=j)
			{
				temp = cow[i];
				break;
				//printf("i=%d j=%d temp=%d\n",i,j,temp);
			}
		}
		if(ans < temp)
			ans = temp;
	}
	printf("%d\n",ans);

	return 0;
}
