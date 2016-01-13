#include<stdio.h>
int main()
{
	int x;
	scanf("%d",&x);
	for(int i=0;i<2;i++)
	{
	int sum=1,n=1;
	for(int i=0;i<x;i++)
	{
		sum=sum*n;
		n++;
	}
	printf("%d",sum);
	scanf("%d",&x);
}
}