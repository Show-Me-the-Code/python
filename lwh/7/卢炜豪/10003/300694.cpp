#include <cstdio>
int a[38][38];
void yh(int n);
int main()
{
    for(int i=1;i<=35;i++)
        a[i][i]=1;
    a[0][0]=0;a[1][0]=0;a[1][1]=1;a[1][2]=0;a[2][1]=1;a[2][2]=1;a[3][1]=1;a[3][2]=2;a[3][3]=1;
    int n;
    while(scanf("%d",&n)==1&&n!=-1)
    {
        for(int i=1;i<=n;i++)
        {
            yh(i);
        }
        printf("\n");
    }
}
void yh(int n)
{
    for(int j=1;j<n;j++)
    {
        a[n][j]=a[n-1][j-1]+a[n-1][j];
        printf("%d ",a[n][j]);
    }
    printf("1\n");
}
