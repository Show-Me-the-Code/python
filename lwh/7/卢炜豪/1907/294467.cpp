#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int T;int val[1000+2][1000+2];
    scanf("%d",&T);
    for(int l=0;l<T;l++)
    {
        int n,w,v,cmax;
        scanf("%d %d",&n,&cmax);
        for(int i=1;i<=n;i++)
        {
            scanf("%d %d",&v,&w);
            for(int j=0;j<=cmax;j++)
            {
                val[i][j]=(i==1? 0:val[i-1][j]);
                if(j>=v)
                    val[i][j]=max(val[i][j],val[i-1][j-v]+w);
            }


        }
        printf("%d\n",val[n][cmax]);
    }
}
