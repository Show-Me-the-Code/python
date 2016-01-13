#include <stdio.h>
int is(int z);
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int w;
        w=n%10;

        if(w!=0)
        {
            is(n);
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
             is(n);
        }
    }
}
int is(int z)
{
    for(;z>0;)
            {
                int q;
                q=z%10;
                z=z/10;
                printf("%d",q);
            }
            printf("\n");
}
