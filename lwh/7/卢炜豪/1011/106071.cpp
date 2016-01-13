#include<stdio.h>
int main()
{
	char c;
	while(scanf(" %c",&c)!=EOF)
	{
		if(c!='y'&&c!='z')
	{
	
		   c=c+2;
		   printf("%c\n",c);
}
		
	else	if(c=='y')
		printf("a\n");
	
	
	else
	
		
        printf("b\n");
    
	
		
	
	}
	return 0;
}