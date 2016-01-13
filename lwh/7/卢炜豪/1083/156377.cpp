#include<stdio.h>
#define maxn 101
int main()
{
    int a[maxn],b[maxn],n;
    while(scanf("%d",&n)==1&&n!=0)
    {
        for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
        for(int i=0;i<n;i++)
        b[i]=a[i];

        for(int i=0;i<n;i++)
        {
            if(a[i]<0)
                a[i]=-a[i];
            else a[i]=a[i];
        }
        for(int i=1;i<n;i++)
        {
            int temp;
            for(int j=0;j<i;j++)
            {
                if(a[i]>a[j])
                    {
                        temp=a[i];
                        a[i]=a[j];
                        a[j]=temp;
                    }
            }

        }
      //  for(int i=0;i<n;i++) printf("%d",a[i]);

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
               if(b[j]>0)
               {
                   if(b[j]==a[i])
                   {
                       if(i==n-1)
                        printf("%d\n",b[j]);
                       else printf("%d ",b[j]);
                   }

               }
               else if(b[j]<=0)
               {
                   if(-b[j]==a[i])
                   {


                    if(i==n-1)
                        printf("%d\n",b[j]);
                       else printf("%d ",b[j]);
                   }
               }

            }
        }

    }
}
