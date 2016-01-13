#include<stdio.h>
int main()
{
	char d[3];
	char a,b,c;
	while(scanf(" %c%c%c",&a,&b,&c)!=EOF)
	{
		d[0]=a;
		d[1]=b;
		d[2]=c;
		
		for(int i=0;i<2;i++)
		{
			int k;k=i+1;char temp;
			if(d[i]>d[k])
			{
				temp=d[i];
				d[i]=d[k];
				d[k]=temp;
				
			}
		
		
			
		}
		for(int i=0;i<=2;i++)
		{
			if(i!=2)
			printf("%c ",d[i]);
			else if(i==2)
			printf("%c",d[i]);
			if(i==2)printf("\n");
		}
	}
}