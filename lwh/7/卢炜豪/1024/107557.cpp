#include<stdio.h>
int main()
{
	int a,b,s;char c;
	while(scanf("%d%c%d=",&a,&c,&b)!=EOF)
	{
		if(c=='+')
		{
			s=a+b;
		}
		else if(c=='-')
		{
			s=a-b;
		}
		else if(c=='*')
		{
			s=a*b;
		}
		else if(c=='/')
		{
			s=a/b;
		}
		else if(c=='%')
		{
			s=a%b;
		}
		
		if(s<0)
		{
			printf("Daddy is bad guy");
		}
		else printf("%d",s);
		printf("\n");
	}
}