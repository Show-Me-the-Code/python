#include <stdio.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int l=n,m=n,w,i,j;
        for(i=0;l>0;i++)
        {
            l/=10;
        }
        //printf("%d\n",i);
        for(;m>0;)
        {
            w=m%10;
            if(w==0)
            {
                m=m/10;
                w=m%10;
                if(w!=0)
                for(;m>0;)
                {
                    printf("%d",w);
                    m=m/10;
                    w=m%10;
                }
            }
            else if(w!=0)
            {

            printf("%d",w);
            m/=10;
            }


        }
        printf("\n");
    }
}
