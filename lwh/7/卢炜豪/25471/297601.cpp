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
        double n;
        scanf("%lf",&n);
        printf("Case #%d: %d\n",v,(int)pow(2,n)%1000000007);
        v++;
    }
    return 0;
}
