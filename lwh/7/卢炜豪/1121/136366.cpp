#include<stdio.h>
#define maxn 55
int main()
{
    int n,sum0=0,sum1=0,sum2=0,sum3=0,l,sum;
    scanf("%d",&n);
    int a[maxn][maxn];

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        scanf("%d",&a[i][j]);

    for(int i=0;i<n;i++)
        sum0=sum0+a[i][n-1];
       // printf("%d\n",sum0);
    for(int i=0;i<n;i++)
        sum1=sum1+a[n-1][i];
       // printf("%d\n",sum1);

    sum=sum0+sum1-a[n-1][n-1];

    for(int i=0,j=n-1;i<n;i++,j--)
    sum2=sum2+a[i][j];
    //printf("%d\n",sum2);
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        sum3=sum3+a[i][j];
    //    printf("%d\n",sum3);

        l=sum3-sum2-sum+a[0][n-1]+a[n-1][0];
        printf("%d\n",l);
}
