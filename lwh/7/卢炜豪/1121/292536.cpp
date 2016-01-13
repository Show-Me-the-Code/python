#include <stdio.h>
int matrix[102][102];
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                scanf("%d",&matrix[i][j]);

        for(int i=0,j=n-1;j>=0;i++,j--)
        {
                matrix[i][j]=0;
        }
        for(int i=0;i<n;i++)
        {
            matrix[n-1][i]=0;
            matrix[i][n-1]=0;
        }
        int sum=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
            sum=sum+matrix[i][j];
        printf("%d\n",sum);

    }
    return 0;
}
