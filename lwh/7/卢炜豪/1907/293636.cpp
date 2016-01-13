#include <cstdio>
int main()
{
    int T;
    scanf("%d",&T);
    for(int z=0;z<T;z++)
    {
        int n,m,w[105],p[105];
        int c[105][105];
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&w[i],&p[i]);
        }
        for(int i=0;i<=m;i++)
        {
            for(int j=0;j<=n;j++)
            {
                if(i<w[i])
                {
                    c[j][i]=c[j-1][i];
                    continue;
                }
                else if(c[j-1][i-w[j]]+p[i]>c[j-1][i])
                {
                    c[j][i]=c[j-1][i-w[i]]+p[i];
                }
                else
                    c[j][i]=c[j-1][i];
            }
        }
        int max=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(c[i][j]>max)
                    max=c[i][j];
            }
        }

        printf("%d\n",max);
    }
    return 0;
}
