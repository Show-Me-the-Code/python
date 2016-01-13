#include<stdio.h>
#define maxn 1005
int main()
{
    int n,m;
    while(scanf("%d %d",&n,&m)==2&&(n!=0&&m!=0))
    {
        int a[maxn],b[maxn];
        for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
        if(n>=m)
        {
        for(int i=0;i<n-m;i++)
        {
            b[i+m]=a[i];
           // printf("b[%d]=%d\n",i+m,b[i+m]);
        }
        for(int i=n-m,j=0;i<n;i++,j++)
        {
            b[j]=a[i];
        }
         for(int i=0;i<n;i++)
        {
           if(i!=n-1)
           printf("%d ",b[i]);
           else printf("%d\n",b[i]);
        }
        }
        else if(n<m)
        {
            printf("%d ",a[n-1]);
            for(int i=0;i<n-1;i++)
               {
                   if(i!=n-2) printf("%d ",a[i]);
                   else printf("%d\n",a[i]);
               }
        }
    }
}
