#include<stdio.h>
int main()
{
	int x,n;
	while(scanf("%d",&x)!=EOF)
	{
		for(int i=1;i<=x;i++)
		{
			int sum=0;
			scanf("%d",&n);
			for(int k=1;k<=n;k++)
			{
				
				sum=k+sum;
			}
			printf("%d\n",sum);
		}
	}
}