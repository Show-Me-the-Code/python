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
            if(a<60||b<60||c<60||d<60)
            {
                count++;
            }
        }
        printf("%d\n",count);
    }
}
