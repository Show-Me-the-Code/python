#include <stdio.h>
#include <string.h>

int main()
{
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        int a[1000+5];
        //memset(a,1,N);
        for(int i=1;i<=N;i++)
            a[i]=-1;
   //     printf("!!=%d\n",a[3]);
        int num=0,flag=-1;
        for(int i=2;i<=N;i++)
        {
            for(int j=1;;j++)
            {
                num=j*i;
                if(num<=N)
                {
                    a[num]=-a[num];
                }
                if(num>N)
                    break;

            }
        }
        a[1]=-1;
    //    for(int i=1;i<=N;i++)
    //        printf("%d ",a[i]);
     //   printf("\n");
     if(N!=1)
        printf("%d",2);
        for(int i=3;i<=N;i++)
        {
            if(a[i]==1)
            {
               // printf("a[%d]=%d ",i,a[i]);

                    printf(" %d",i);

            }
        }
     printf("\n");
    }
    return 0;
}
