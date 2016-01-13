#include<stdio.h>
int main()
{
	int sum=0,x,n=1;
	while(scanf("%d",&x)!=EOF)
	{
		if(x>0)
		{
		
		for(int i=0;i<x;i++)
		{
			sum=sum+n;
			n++;
		}
		printf("%d\n",sum);
		sum=0;
		n=1;
	}
		else 
		{
		
		for(int i=0;i<x;i++)
		{
			sum=sum+n;
			n++;
		}
		printf("%d\n",-sum);
		sum=0;
		n=1;
	}
	}
	
}