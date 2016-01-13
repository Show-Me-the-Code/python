#include<stdio.h>
#include<math.h>
int main()
{
	int x;int i=0;int s;
	while(scanf("%d",&x)!=EOF)
	{
		
		int n;
		s=sqrt(x);
		for(n=1;n<=s;n++)
		{
			if(x%n==0)
				i++;
		}
		if(i!=1)
			printf("no\n");	
		else 
			printf("yes\n");
		i=0;
		
	
	
}
return 0;
}
