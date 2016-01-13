#include <stdio.h>

int main()
{
    int n,a[81][81];
    while(scanf("%d",&n)==1)
    {
        int up=0,down=0;

        if(n==0) break;

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                scanf("%d",&a[i][j]);
        }




            for(int i=0;i<n-1;i++)
            {
                for(int j=i+1;j<n;j++)
                {
                    if(a[i][j]==0)
                        up++;

                }
            }
           // printf("%d\n",up);

             for(int i=1;i<n;i++)
            {
                for(int j=0;j<i;j++)
                {
                    if(a[i][j]==0)
                        down++;
                       // printf("i=%d j=%d ",i,j);

                }
            }

          //  printf("up=%d down=%d \n",up,down);
           if(up==down)
            printf("NO\n");

            else if((up>=0&&up<n*(n-1)/2)&&(down==n*(n-1)/2))
                printf("UP\n");

            else if((up==n*(n-1)/2)&&(down>=0&&down<n*(n-1)/2))
                printf("DOWN\n");
            else printf("NO\n");

    }
}
