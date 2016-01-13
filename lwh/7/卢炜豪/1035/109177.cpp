#include<stdio.h>
#include<math.h>
int main()
{
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		int c[n],k;
   	    int q=pow(10,n-1);
   	    int z=pow(10,n)-1;
	//	printf("%d\n",q);
	//	printf("%d\n",z);
		for(int i=q;i<=z;i++)
		{
			k=i;
			int sum0=0;
			for(int j=0;k>0;j++)
			{
				c[j]=k%10;
				k/=10;
				
			}
			for(int h=n-1;h>=0;h--)
			{
				
				sum0=pow(c[h],n)+sum0;
			}
			if(sum0==i)
			printf("%d\n",i);
			
			
		}
	}
}