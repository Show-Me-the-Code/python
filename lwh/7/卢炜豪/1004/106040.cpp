#include<stdio.h>
int main()
{
	int x,i,n=1,sum=1;
	while(scanf("%d",&x)!=EOF)
	{
		for(i=0;i<x;i++)
		{
			sum=sum*n;
			n++;
		}
		printf("%d\n",sum);
	}
	return 0;
}