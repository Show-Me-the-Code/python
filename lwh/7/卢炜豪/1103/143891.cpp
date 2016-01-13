#include<stdio.h>
#define maxn 105
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n)==2&&(m!=0&&n!=0))
    {
        int a[maxn][maxn];
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
            scanf("%d",&a[i][j]);

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            printf("%d ",a[j][i]);
            printf("\n");
        }
        printf("\n");
    }
}
