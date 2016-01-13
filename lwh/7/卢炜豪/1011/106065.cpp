#include<stdio.h>
int main()
{
	char c;
	while(scanf(" %c",&c)!=EOF)
	{
		if(c!='y'||c!='z')
		{
		   c=c+2;
		   printf("%c\n",c);
}
		if(c=='y')
		{
		
		c='a';
		printf("%c\n",c);
	}
	
		if(c=='z')
	{
		c='b';
        printf("%c\n",c);
    }
	
		
	
	}
	return 0;
}