#include <Stdio.h>

int main()
{
    int n,a[81][81];
    while(scanf("%d",&n)==1)
    {
        int up=0;

        if(n==0) break;

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                scanf("%d",&a[i][j]);
        }

        if(a[0][n-1]!=0&&a[n-1][0]!=0)
            {
                printf("NO\n");
            }

        else
        {
            for(int i=0;i<n-1;i++)
            {
                for(int j=i+1;j<n;j++)
                {
                    if(a[i][j]==0)
                        up++;

                }
            }
           // printf("%d\n",up);

            if(up==n*(n-1)/2)
                printf("DOWN\n");

            else
                printf("UP\n");



        }
    }
}
