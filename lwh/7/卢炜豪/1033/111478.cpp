#include<stdio.h>

int main()
{
     int  m,n;
    while(scanf("%d %d",&m,&n)!=EOF)
    {
        long long int sum0,sum1;sum0=sum1=0;
        int num=n-m+1;int a[num*1000];
        for(int i=0;i<num;i++)
        {
           if(m<=n)
           {
               a[i]=m;
               m++;
           }
       //   printf("a[%d]=%d ",i,a[i]);
        }
    //  printf("\n");
        for(int i=0;i<num;i++)
        {
            if(a[i]%2==0)
            {
                sum0=a[i]*a[i]+sum0;
            }
            else if(a[i]%2!=0)
            {
                sum1=a[i]*a[i]*a[i]+sum1;
            }
        }
        printf("%lld %lld\n",sum0,sum1);

    }

}
