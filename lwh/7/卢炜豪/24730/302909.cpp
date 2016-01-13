#include <stdio.h>
#include <string.h>
#include <math.h>
#define maxn 100000+10
int main()
{
    double N,M,Q,x,y,z;
    while(scanf("%lf",&N)!=EOF)
    {

        double ans=log(N*2.09);
        int ans0=log(N*2.09);
        if(ans0-ans>0)
            ans0++;
        printf("%d\n",ans0);

    }

    return 0;
}
