#include<stdio.h>
int main()
{
     int n;
    while(scanf("%lld",&n)!=EOF)
    {
        int i,q=n,t;
        if(n==0) printf("0");
        for(i=0;n>0;i++)
        {
            n=n/10;
        }
        int a[i];
        for(t=0;t<i;t++)
        {
            a[t]=q%10;
            q=q/10;
            //printf("a[%d]=%d ",t,a[t]);
        }
        if(a[0]!=0)
        {
            for(t=0;t<i;t++)
                printf("%d",a[t]);
            printf("\n");
        }
        if(a[0]==0)
        {
           int b=1;
           while(b<i)
           {
               if(a[b]==0)
               {
                   b=b+1;
               }
               else if(a[b]!=0)
               {
                   for(int k=b;k<i;k++)
                   {
                       printf("%d",a[k]);
                   }
                   printf("\n");
                   break;

               }
               b++;
           }
        }

    }
}
