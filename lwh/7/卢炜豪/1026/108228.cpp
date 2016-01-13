#include<stdio.h>
#include<math.h>
int main()
{
	double x,y,z,area,p,a,b,c;
	while(scanf("%lf %lf %lf",&x,&y,&z)!=EOF)
	{
		a=x+y;b=x+z;c=y+z;
		if(((x+y)>z)&&((x+z)>y)&&((y+z)>x)&&((x-y)<z)&&((x-z)<y)&&((y-z)<x))
		{
			p=(0.5)*(x+y+z);
			area=sqrt(p*(p-x)*(p-y)*(p-z));
			printf("%.2lf\n",area);
		}	
		else printf("not a triangle\n");
		
		
		
	}
}