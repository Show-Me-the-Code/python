#include <stdio.h>
#include <string.h>
#include <math.h>
#define maxn 100000+10
int main()
{
    double N,M,Q,x,y,z;
    while(scanf("%lf",&N)!=EOF)
    {
        double ans=log(N)/log(3);
        printf("%.0lf\n",ans+0.6);
    }

    return 0;
}
