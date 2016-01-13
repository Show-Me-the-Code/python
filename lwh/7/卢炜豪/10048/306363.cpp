#include <cstdio>
int main()
{
    double a,b;
    while(scanf("%lf %lf",&a,&b)==2)
    {
        double j = a;double k = b/a;
        printf("%.2lf %.2lf\n",(j+k)/2,(j-k)/2);
    }
}
