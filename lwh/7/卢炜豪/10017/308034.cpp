#include <cstdio>
#include <cstring>
#include <cmath>
int main()
{
    double D,d,r1=D/2,r2=d/2,s;
    int T;scanf("%d",&T);
    while(T--)
    {
        scanf("%lf %lf %lf",&D,&d,&s);
        double t = D/2-d/2,q = d+s;
        double a = (2*pow(t,2)-pow(q,2))/(2*pow(t,2));
        double b = acos (a);
        double ans = 2*acos(-1.0)/b;
        printf("%d\n",(int)ans);
    }
}
