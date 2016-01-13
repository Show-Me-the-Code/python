#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int g[1000000+5];
int main()
{
    int T,v=1;
    scanf("%d",&T);
    while(v<=T)
    {
        int sum=0;
        g[0]=1;g[1]=1;g[2]=3;
        int n;scanf("%d",&n);
        for(int i=3;i<=n;i++)
            g[i]=g[i-1]+i;
        for(int i=1;i<=n;i++)
            sum=sum+g[i];
            printf("Case #%d: %d\n",v,sum%1000000007);

        v++;
    }
    return 0;
}
