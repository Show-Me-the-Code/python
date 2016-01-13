#include<stdio.h>
#define maxn 100000
int main()
{
    int n,r,a[maxn],index,dd;
    char c[6]={'A','B','C','D','E','F'};
    while(scanf("%d %d",&n,&r)!=EOF)
    {
        if(r==2)
        {
            dd=n;
            n=-n;
            if(n==1||n==0) printf("%d\n",n);
           else
           {
           for(int i=0;n!=0;i++)
           {
               int w;
               w=n%2;
               a[i]=w;
               n=n/2;
               index=i;
           }
           if(dd<0) printf("-");
           for(int i=index;i>=0;i--)
           {

               printf("%d",a[i]);
               }
           printf("\n");
           }
        }

        else if(r!=2&&r<=9)
        {
             dd=n;
             n=-n;
            if(n<r&&n>=0) printf("%d\n",n);
            else
            {


             for(int i=0;n!=0;i++)
           {
               int w;
               w=n%r;
               a[i]=w;
               n=n/r;
               index=i;
           }
            if(dd<0) printf("-");
           for(int i=index;i>=0;i--) printf("%d",a[i]);
           printf("\n");
         }
        }
         else if(r>10)
         {
             dd=n;
             n=-n;
             for(int i=0;n!=0;i++)
           {
               int w;
               w=n%r;
               a[i]=w;
               n=n/r;
               index=i;
           }
            if(dd<0) printf("-");
           for(int i=index;i>=0;i--)
           {
               if(a[i]<10)
               printf("%d",a[i]);
               else if(a[i]>=10)
               {
                   int t=a[i]%10;
                   printf("%c",c[t]);
               }
           }
           printf("\n");
         }

        }
    }
