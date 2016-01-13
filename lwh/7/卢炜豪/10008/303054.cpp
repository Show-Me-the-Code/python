#include <stdio.h>
#include <string.h>

int main()
{
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        int a[1000+5];
        memset(a,0,N);
        int num=2,flag=-1;
        for(int i=2;i<=N;i++)
        {
            for(int j=1;j<=i;j++)
            {
                num=i*j;
                if(num<=N)
                a[num]=-flag;
            }
        }
        for(int i=1;i<=N;i++)
        {
            if(a[i])
            {
                if(i!=N)
                    printf("%d ",i);
                else
                    printf("%d\n",i);
            }
        }
    }
    return 0;
}
