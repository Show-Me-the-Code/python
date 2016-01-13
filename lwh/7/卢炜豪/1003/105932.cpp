#include<Stdio.h>
int main()
{
	int x,sum=1,n=1;
	scanf("%d",&x);
	for(int i=0;i<x;i++)
	{
		
		sum=sum*n;
		n++;
		
	}
	printf("%d\n",sum);
}