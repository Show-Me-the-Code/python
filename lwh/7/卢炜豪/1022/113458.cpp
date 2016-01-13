#include<stdio.h>
int main()
{
    long long int n;
    while(scanf("%lld",&n)!=EOF)
    {
        int i;long long q=n;
        if(n==0) printf("0");
        for(i=0;n>0;i++)
        {
            n=n/10;
        }
        int a[i];
        for(int t=0;t<i;t++)
        {
            a[t]=q%10;
            q=q/10;
            if(a[t]!=0)
            printf("%d",a[t]);
        }
        printf("\n");
    }
}
