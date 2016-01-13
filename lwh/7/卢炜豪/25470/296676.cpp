#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
long long int g[1000000+5];
long long int f[1000000+5];
int main()
{
    int T,v=1;
    scanf("%d",&T);
    while(v<=T)
    {
        f[1]=3;f[2]=6;
        int n;
        scanf("%d",&n);
        for(int i=3;i<=n;i++)
            f[i]=f[i-1]+i+1;
   //         printf("%lld\n",f[n]);
        g[1]=1;g[2]=4;
        for(int i=3;i<=n;i++)
            g[i]=g[i-1]+f[i-1];
            printf("Case #%d: %lld\n",v,g[n]%1000000007);

        v++;
    }
    return 0;
}
