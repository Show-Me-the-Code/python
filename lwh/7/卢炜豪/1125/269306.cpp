#include <stdio.h>
#include <string.h>
#define maxn 20+2
int main()
{
    int T,t,a[maxn],b[maxn],c[maxn];
   // memset(b,1,sizeof(b));
    while(scanf("%d",&T)!=EOF)
    {
        for(int count=0;count<T;count++)
        scanf("%d %d",&a[count],&c[count]);

        long long int M=1;
        for(int i=0;i<T;i++)
            M=M*a[i];

        //先求数论倒数吧，用b[i]存
        int ti;
        for(int i=0;i<T;i++)
        {
            for(ti=1;;)
            {
            int Mi=M/a[i];
            if((ti*Mi)%a[i]==1)
             {
                 b[i]=ti;
                 break;
             }
            else
            ti++;
            }
         //   printf("%d\n",b[i]);
        }
        //求得数论倒数了

        int sum1=0;
        for(int i=0;i<T;i++)
        sum1=b[i]*(M/a[i])*c[i]+sum1;
     //   printf("%d\n",sum1);
        int sum2=0,k;
        for(k=1;;)
        {
            sum2=sum1-k*M;
            if(sum2<0)
            {
                k=k-1;
                break;
            }
            else
                k++;
        }
        printf("%d\n",sum1-k*M);


    }
}
