#include<stdio.h>
int main()
{
    int sum=0,x,n=1;
	while(scanf("%ld",&x)!=EOF)
	{
		if(x>0)
		{
		
		for(int i=0;i<x;i++)
		{
			sum=sum+n;
			n++;
		}
		printf("%ld\n",sum);
		sum=0;
		n=1;
	}
		else if(x<=0)
		{
		
		for(int i=0;i<-x;i++)
		{
			sum=sum+n;
			n++;
		}
		printf("%ld\n",-sum+1);
		sum=0;
		n=1;
	}
	}
	
}