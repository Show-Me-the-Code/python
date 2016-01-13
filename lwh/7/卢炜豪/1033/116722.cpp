#include<stdio.h>
int main()
{
    int x,y,temp,sum0,sum1;
    while(scanf("%d %d",&x,&y)!=EOF)
    {

        sum0=sum1=0;
        if(x>y)
        {
          temp=y;
          y=x;
          x=temp;
        }
        for(;x<=y;x++)
        {
            if(x%2==0)
                sum0=sum0+x*x;
            if(x%2!=0)
                sum1=sum1+x*x*x;
        }
        printf("%d %d\n",sum0,sum1);
    }
}
