#include<stdio.h>
int main()
{
	double t,f;
	while(scanf("%lf",&f)!=EOF)
	{
		t=5.0*(f-32.0)/9;
		printf("%.2lf\n",t);
	}
	return 0;
}