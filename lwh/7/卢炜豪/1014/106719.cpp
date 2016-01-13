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
		int k,index,i;
		char temp;
		for(k=0;k<2;k++)
		{
			
		index=k;
		for(i=k+1;i<3;i++)
		if(d[i]<d[index])
		index=i;
		temp=d[index];
		d[index]=d[k];
		d[k]=temp;
}
	
		for(int i=0;i<3;i++)
		{
	     	if(i!=2)
			printf("%c ",d[i]);
		    else if(i==2)
			printf("%c",d[i]);
			if(i==2)printf("\n");
		}
	}
}