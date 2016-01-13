#include <stdio.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int w;
        w=n%10;

        if(w!=0)
        {
            for(;n>0;)
            {
                int q;
                q=n%10;
                n=n/10;
                printf("%d",q);
            }
            printf("\n");
        }

        else if(w==0)
        {
             for(;;)
             {
                 w=n%10;

                 if(w!=0)
                    break;
                n=n/10;
             }
             for(;n>0;)
            {
                int q;
                q=n%10;
                n=n/10;
                printf("%d",q);
            }
            printf("\n");
        }
    }
}
