#include <cstdio>
#include <cmath>
double f(double x);
double y;
using namespace std;
int main()
{
    while(scanf("%lf",&y)!=EOF)
    {
        double x,a=-70,b=70,end=0.001;
        double fx=3*x*x*x+2*x-y;
        while(1)
        {
            if(y==0)
            {
                printf("0\n");
                break;
            }
            if(f(a)*f(b)<=0)
            {
                if(f(a)==0)
                    printf("%.3lf\n",a);
                else if(f(b)==0)
                    printf("5.3lf\n",b);
                else if(f(a)*f(b-(b-a)/2)<0)
                {
                    a=a;
                    b=b-(b-a)/2;
               //     printf("1\n");
                }
                else if(f(b-(b-a)/2)*f(b)<0)
                {
                   a=b-(b-a)/2;
                   b=b;
                //   printf("2\n");
                }
                if(fabs(f(a)-0)<=end)
            {
                printf("%.3lf\n",a);
                break;
            }
            }
             //   printf("3\n");
        }


    }
    return 0;
}
double f(double x)
{
    double fx=3*x*x*x+2*x-y;
    return fx;
}
