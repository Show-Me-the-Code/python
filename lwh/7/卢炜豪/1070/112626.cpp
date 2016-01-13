#include<stdio.h>
int main()
{
    int n;
    while(1)
    {
        int sum0=0,sum1=0,sum2=0;
        scanf("%d",&n);
        double x;double a[n];
        if(n==0) break;
        for(int i=0;i<n;i++)
        {
                scanf("%lf",&x);
                a[i]=x;
        }
        for(int i=0;i<n;i++)
        {
            if(a[i]<0) sum0++;
            else if(a[i]==0) sum1++;
            else if(a[i]>0) sum2++;
        }
        printf("%d %d %d\n",sum0,sum1,sum2);
    }
}
