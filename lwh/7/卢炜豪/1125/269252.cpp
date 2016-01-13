#include <stdio.h>

#define maxn 20+2
int main()
{
    int T,t,a[maxn],b[maxn],c[maxn];
    while(scanf("%d",&T)!=EOF)
    {
        for(int count=0;count<T;count++)
        scanf("%d %d",&a[count],&c[count]);

        int M=1;
        for(int i=0;i<T;i++)
            M=M*a[i];

        int sum=0;
        for(int i=0;i<T;i++)
          {
            b[i]=M/a[i];
            t=b[i]%a[i];
            b[i]=b[i]*t*c[i];
            sum=sum+b[i];
           // printf("%d\n",b[i]);
          }
        int sum1=sum,book;
        for(int k=1;;k++)
        {

            sum1=sum-k*M;
            if(sum1<0)
            {
                book=k-1;
                break;
            }
        }
        printf("%d\n",sum-book*M);







    }
}
