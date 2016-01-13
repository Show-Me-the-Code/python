#include<stdio.h>
int main()
{
    int x;
    while(scanf("%d",&x)!=EOF)
    {
        int t=x;
        int i;
        if(x>0)
        {
        for(i=0;x>0;i++)
        {
            x=x/10;
        }
        }
       else  if(x<0)
        {
            x=-x;
             for(i=0;x>0;i++)
        {
            x=x/10;
        }

        }
        else if(x==0) i=1;
        printf("%d ",i);
        printf("%d\n",t%3);

    }
}
