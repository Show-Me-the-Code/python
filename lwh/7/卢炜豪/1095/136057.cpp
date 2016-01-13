#include<stdio.h>
#define maxn 1005
int main()
{
    int n,m;
    while(scanf("%d %d",&n,&m)==2)
    {
        if(n==0&&m==0) break;
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



            if(2*n-m>=0)
           {
            for(int i=2*n-m;i<n;i++)
            printf("%d ",a[i]);
            for(int i=0;i<2*n-m;i++)
            {
                if(i!=2*n-m-1) printf("%d ",a[i]);
                else printf("%d\n",a[i]);
            }
           }
           else if(2*n-m<0)
           {
               if(m%2==0)
               {
                   m=n+2;
                    for(int i=2*n-m;i<n;i++)
            printf("%d ",a[i]);
            for(int i=0;i<2*n-m;i++)
            {
                if(i!=2*n-m-1) printf("%d ",a[i]);
                else printf("%d\n",a[i]);
            }
               }
               else if(m%2!=0)
               {
                   m=n+3;
                    for(int i=2*n-m;i<n;i++)
            printf("%d ",a[i]);
            for(int i=0;i<2*n-m;i++)
            {
                if(i!=2*n-m-1) printf("%d ",a[i]);
                else printf("%d\n",a[i]);
            }
               }
           }




        }
    }
}
