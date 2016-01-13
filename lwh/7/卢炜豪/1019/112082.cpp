#include<stdio.h>
void down(int n);
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int t=n;
        for(int i=1;i<=n;i++)
        {

            for(int j=t-1;j>0;j--)
            {
                printf(" ");
            }
            for(int k=2*i-1;k>0;k--)
            {
                printf("*");
            }
            printf("\n");
            t--;

        }
         down(n);

    }
}
void down(int n)
{
   int s=2*n-1;int j=s;
   int h=n-1;
   for(int t=1;t<=h;t++)
   {
       for(int i=1;i<=t;i++)
       {
           printf(" ");
       }

       for(int q=j-2;q>0;q--)
       {
           printf("*");
          }
          j=j-2;
       printf("\n");
   }
}
