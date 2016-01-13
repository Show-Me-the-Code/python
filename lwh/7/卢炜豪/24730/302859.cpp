#include <stdio.h>
#include <string.h>
#include <math.h>
#define maxn 100000+10
int main()
{
    int N,M,Q,x,y,z;
    while(scanf("%d",&N)!=EOF)
    {
        int ans;
        if(N<=3)
            ans=1;
        else if(N<=9)
            ans=2;
        else if(N<=27)
            ans=3;
        else if(N<=81)
            ans=4;
        else if(N<=243)
            ans=5;
        else if(N<=729)
            ans=6;
        else
            ans=7;
        printf("%d\n",ans);
    }

    return 0;
}
