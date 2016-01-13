#include <stdio.h>
#include <string.h>
#include <math.h>
#define maxn 100000+10
int main()
{
    double N,M,Q,x,y,z;
    while(scanf("%lf",&N)!=EOF)
    {
        if(N==1)
            printf("1\n");
        else
        {
        double ans=log(N*2.09);
        printf("%d\n",(int)ans);
        }
    }

    return 0;
}
