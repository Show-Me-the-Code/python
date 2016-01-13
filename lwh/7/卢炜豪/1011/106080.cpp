#include<stdio.h>
int main()
{
	char ch;
	while(scanf(" %c",&ch)!=EOF)
	{
		if(ch>='a'&&ch<'y')
		{
			ch=ch+2;
		}
		if(ch=='y')
		{
			ch='a';
		}
		if(ch=='z')
		{
			ch='b';
		}
		printf("%c\n",ch);
		
	}
	return 0;
}