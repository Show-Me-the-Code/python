#include<stdio.h>
int main()
{
	const double PI=3.1415927;
	double r;
	while(scanf("%lf",&r)!=EOF)
	{
		double area;
		area=PI*r*r;
		printf("%.2f\n",area);
	}
}