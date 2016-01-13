#include<stdio.h>
#include<math.h>
int main()
{
	int a,n,s,sum=0;
	while(scanf("%d %d",&a,&n)!=EOF)
	{
		while(n!=0)
		{
		for(int i=n-1;i>=0;i--)
		{
			s=pow(10,i);
			sum=sum+a*s;
		}
	
		n--;
		}
		printf("%d\n",sum);
		sum=0;


	}
	return 0;
}