#include <stdio.h>
#include <string.h>
#include <math.h>
#define maxn 100000+10
int main()
{
    double N,M,Q,x,y,z;
    while(scanf("%lf",&N)!=EOF)
    {
        int ans1=log(N)/log(3);
        double ans=log(N)/log(3);
        if(ans-ans1>0)
            ans1++;
        printf("%d\n",ans1);
    }

    return 0;
}
