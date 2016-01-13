#include<stdio.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n==0) printf("0\n");
        else
      {

        int w;
        w=n%10;
        if(w==0)
        {
            for(;w==0;)
            {
                n=n/10;
                w=n%10;
            }
            for(;n>0;n=n/10) printf("%d",n%10);
            printf("\n");
         }
         else if(w!=0)
         {
            for(;n>0;n=n/10) printf("%d",n%10);
            printf("\n");
         }
      }
    }
}
