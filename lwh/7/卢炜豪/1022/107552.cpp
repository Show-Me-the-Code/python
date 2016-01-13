#include<stdio.h>
int main()
{
	int n,x;
	while(scanf("%d",&x)!=EOF)
	{
		while(x>0)
		{
			n=x%10;
			x=x/10;
			if(n!=0)
			{
				printf("%d",n);
			}
			else if(n==0)
			{
				n=x%10;
				while(n!=0)
				{
				 	 printf("%d",n);
			   	  	x=x/10;
			   	  	n=x%10;
			}
		
		
		}
		}
		printf("\n");	
		}
		
		

	} 
