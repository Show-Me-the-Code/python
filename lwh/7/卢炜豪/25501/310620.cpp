/*
    因为每次减去某个数的时候都是在相邻两格进行（看成黑白格的话就意味着每次都会有黑格与白格减去相同是数目

    当减到都为0时，减去的数目是相同的，即白格减去的总数与黑格减去的总数相等。（暂时可以推出黑格总数等于白格总数）
*/
#include <cstdio>
#define maxn 100+5
int main()
{
    int n,m;
    while(scanf("%d %d",&n,&m)==2)
    {
        if(n==0&&m==0)
            return 0;
        int a[maxn][maxn],white=0,black=0;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                scanf("%d",&a[i][j]);
                if((i+j)%2==0)
                    black+=a[i][j];
                else
                    white+=a[i][j];
            }
        }
        //printf("white=%d black=%d\n",white,black);
        if(black==white)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
