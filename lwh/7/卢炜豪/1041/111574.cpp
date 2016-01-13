#include<stdio.h>
int main()
{
    int t,x;
    scanf("%d",&t);
    scanf("%d",&x);
    for(int i=1;i<=t;i++)
    {
        int count=0;
        for(int j=1;j<=x;j++)
        {
            int a,b,c,d;
            scanf("%d %d %d %d",&a,&b,&c,&d);
            int sum[4]={a,b,c,d};
            for(int q=0;q<4;q++)
            {
                if(sum[q]<60)
                    count++;
            }
        }
        printf("%d\n",count);
    }
}
