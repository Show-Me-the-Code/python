#include<stdio.h>
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n)==2&&(m!=0&&n!=0))
    {
        int sum=0,w=0;
        int a[m][n];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
       /* for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                printf("%d ",a[i][j]);
            }
            printf("\n");
        }
        printf("\n\n");
*/
        for(int i=0;i<n;i++)
        {
            int h=0;
            for(int j=0;j<m;j++)
            {
                sum=sum+a[h][i];
                h++;
            }
            printf("%d ",sum);
            sum=0;
        }
        printf("\n");

    }
}
