#include <stdio.h>

int gcd(int x,int y);
int main()
{
    int ai,bi,n;
    while(scanf("%d",&n)!=EOF)
    {
        int x=0,y=1;
        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&ai,&bi);
            for(;;)
            {

                if(x%ai==bi)
                    break;
                x=x+y;

            }

            y=y*ai/gcd(ai,y);


        }
        printf("%d\n",x);
    }
}

int gcd(int x,int y)
{
  return y==0 ? x : gcd(y,x%y);
}
