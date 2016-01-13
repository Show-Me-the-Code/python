#include<stdio.h>
#include<string.h>
int main()
{
    int n,a[105][105];
    while(scanf("%d",&n)==1&&n!=-1)
    {
        memset(a,0,sizeof(a));
        //a[0][0]=1;
        int x=0,y=0,sum=1;
        while(1)
        {

            while(a[x][y]==0&&y<=n-1)
            {
                a[x][y]=sum;
                y++;
                sum++;
                //printf("%d\n",sum);
            }
            if(sum==n*n+1) break;
           //printf("→ x=%d y=%d sum=%d\n",x,y,sum);

           x=x+1;
           y=y-1;
           while(a[x][y]==0&&x<=n-1)
           {
               a[x][y]=sum;
             //  printf("%d\n",sum);
                x++;
               sum++;
           }
              if(sum==n*n+1) break;
            //printf("↓ x=%d y=%d sum=%d\n",x,y,sum);
           x=x-1;
           y=y-1;
           while(a[x][y]==0&&y>=0)
           {
               a[x][y]=sum;
               y--;
               sum++;
           }
              if(sum==n*n+1) break;
           //printf("← x=%d y=%d sum=%d\n",x,y,sum);
           x=x-1;
           y=y+1;
           while(a[x][y]==0&&x>=0)
           {
               a[x][y]=sum;
               x--;
               sum++;
           }
           // printf("↑ x=%d y=%d sum=%d\n",x,y,sum);
              x=x+1;
              y=y+1;


        //   printf("sum=%d\n",sum);
        }




          for(int i=0;i<n;i++)
           {
            for(int j=0;j<n-1;j++)
           {
               printf("%d ",a[i][j]);
           }
           printf("%d\n",a[i][n-1]);
           }
           printf("\n");
    }
}
