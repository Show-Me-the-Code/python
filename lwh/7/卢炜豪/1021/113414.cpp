#include<stdio.h>
int main()
{
    long long int n;
    while(scanf("%lld",&n)!=EOF)
    {
        int i;int t=n;int q;
        for(i=0;n>0;i++)
        {
            n=n/10;

        }

        int a[i];
        for(int j=0;j<i;j++)
        {
            q=t%10;
            t=t/10;
            a[j]=q;
        }
        for(int k=i-1;k>=0;k--)
        {
            if(k!=0) printf("%d ",a[k]);
            else if(k==0) printf("%d\n",a[k]);
        }

    }
}
