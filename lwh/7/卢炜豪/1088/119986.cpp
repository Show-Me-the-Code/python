#include<stdio.h>
int main()
{
    int M;
    scanf("%d",&M);
    for(int i=0;i<M;i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        int sum0=0,sum1=0;

        for(int m=1;m<a;m++)
        {
            if(a%m==0)
                sum0=sum0+m;
        }
        for(int n=1;n<b;n++)
        {
            if(b%n==0)
                sum1=sum1+n;
        }
        if(sum0==b&&sum1==a)
            printf("YES\n");
        else printf("NO\n");
    }
}
