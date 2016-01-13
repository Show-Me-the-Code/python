#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int T,v=1;
    scanf("%d",&T);
    while(T--)
    {
        int add=1;
        double n;
        scanf("%lf",&n);
        for(int i=0;i<n;i++)
            add=add*2%1000000007;
        printf("Case #%d: %d\n",v,add);
        v++;
    }
    return 0;
}
