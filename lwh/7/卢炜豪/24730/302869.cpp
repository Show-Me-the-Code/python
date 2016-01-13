#include <stdio.h>
#include <string.h>
#include <math.h>
#define maxn 100000+10
int main()
{
    int N,M,Q,x,y,z;
    while(scanf("%d",&N)!=EOF)
    {
        if(N==1)
            printf("1\n");
        else
        {
        int ans=log(N*2.09);
        printf("%d\n",ans);
        }
    }

    return 0;
}
