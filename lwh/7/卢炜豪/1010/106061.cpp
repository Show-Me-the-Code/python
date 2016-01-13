#include<stdio.h>
int main()
{
	double x;
	while(scanf("%lf",&x)!=EOF)
	{
		if(x>=0) printf("%.2f\n",x);
		else printf("%.2lf\n",-x);
	}
}