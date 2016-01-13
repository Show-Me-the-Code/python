#include<stdio.h>
int main()
{
    int x;
    while(1)
    {
        scanf("%d",&x);
        int sum=0;
        if(x==0)
        {
              break;
        }
        for(int i=1;x>0;i++)
        {
            int w;
            w=x%10;
            sum=sum+w;
            x=x/10;
        }
        printf("%d\n",sum);


    }
}
