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
			int k;k=i+1;int t;
			if(d[i]>d[k])
			{
				t=i;
				i=k;
				k=i;
			}
		}
		for(int i=2;i>=0;i--)
		{
			printf("%c ",d[i]);
			if(i==0)printf("\n");
		}
	}
}