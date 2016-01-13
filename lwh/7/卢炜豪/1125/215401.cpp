#include<stdio.h>
#define maxn 1005
int main()
{
    int a[maxn][2],n;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=0;i<n;i++)
            for(int j=0;j<2;j++)
            scanf("%d",&a[i][j]);
       // int count=0;
        int i;
        for(i=(a[n-1][0]+a[n-1][1]);;i++)
        {
             int count=0;
            for(int j=0;j<n;j++)
            {

                if(i%a[j][0]==a[j][1]) count++;
                else break;

            }
         //  printf("count=%d i=%d\n",count,i);
            if(count==n)
                break;
        }
        printf("%d\n",i);

    }
}
