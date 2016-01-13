#include<stdio.h>
int main()
{
	int n,i=0,q=7;
	while(scanf("%d",&n)!=EOF)
	{
		if(n%7==0)
		{
			printf("YES\n");
		}
		else if(n%7!=0)
		{
			int k,p;
			if(n>10)
			{
			
			for(;n>10;)
			{
				p=n%10;
				if(p%7==0)
				{
					printf("YES\n");
					break;
				}
				else n=n/10;
			}
		}
			else if(n<=10)
			{
				printf("NO\n");
			}
			}
		
		}
	
}