#include<stdio.h>
int main()
{
	int x;
	while(scanf("%d",&x)!=EOF)
	{
		int sum=1,n=1;
		for(int i=0;i<x;i++)
		{
			sum=sum*n;
			n++;
		}
		printf("%d\n",sum);
	}
}