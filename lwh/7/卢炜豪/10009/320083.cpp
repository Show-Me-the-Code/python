#include <cstdio>
#include <cmath>
double f(double x); //计算f(x)的值
double y;			//把题目中的y设成全局变量
using namespace std;
int main()
{
    while(scanf("%lf",&y)!=EOF)
    {
        double x,a=-200,b=200,end=0.001;  //因为fabs(y)<=7000000,也就意味着x值的范围会在(-200,200)的范围内。a,b分别表示区间的左右端点
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
