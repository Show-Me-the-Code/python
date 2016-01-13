#include<stdio.h>
int main()
{
	int a,b,c,d,x;
	while(scanf("%d",&x)!=-1)
	{
	    d=x;
		for(int i=0;i<x;i++)
		{
			
			for(int j=0;j<d-1;j++)
			{
			
			printf(" ");
			
			
		}
			for(int k=0;k<i+1;k++)
			{
				if(i==0)
				{
				
				printf("*");
			}
			else if(i!=0)
				{
					if(k==i)
					{
						printf("*");
						
					}
					else printf("* ");
					
				}
				}
		d--;
		printf("\n");
		}
		printf("\n");
	}
	
}