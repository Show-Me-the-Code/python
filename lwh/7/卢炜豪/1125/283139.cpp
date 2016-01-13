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
  //  printf("x=%d y=%d\n",x,y);
    while(y!=0)
    {
       int temp=x;
       x=y;
       y=temp%y;
    }
  //  printf("return=%d\n",x);
    return x;
}
