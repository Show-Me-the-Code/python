#include<stdio.h>
#define maxn 11
int main()
{
    long long int x;int a[maxn];
    while(scanf("%lld",&x)!=EOF)
    {
        int i,j;int k=x;
        for(i=0;k>=1;i++)
        {
            j=k%10;
            k=k/10;
            a[i]=j;
           // printf("%d ",a[i]);
        }
       // printf("i=%d\n",i);
     for(int k=i-1;k>=0;k--)
        {
            if(k!=0)
            {
                printf("%d ",a[k]);
            }
            else if(k==0)
            {
                printf("%d\n",a[k]);
            }
        }

    }
}
