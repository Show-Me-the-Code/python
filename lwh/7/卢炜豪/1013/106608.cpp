#include<stdio.h>
int main()
{
	int a,b,c;
	while(scanf("%d %d %d",&a,&b,&c)!=EOF)
	{
		if(a>b)
		{
			if(c>=a)
			printf("%d\n",c);
			else if(a>c)
			printf("%d\n",a);
		}
		if(a<b)
		{
			if(c>=b)
			printf("%d\n",c);
			else if(c<b)
			printf("%d\n",b);
		}
		if(a==b)
		{
			if(c==a)
			printf("%d\n",c);
			
		}
	}
	return 0;
}