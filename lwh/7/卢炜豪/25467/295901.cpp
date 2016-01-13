#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int n;long long c[10000+5];
        c[0]=0;int max=-1;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lld",&c[i]);
        sort(c,c+n);
        long long int sum=0;
        for(int i=1;i<n;i++)
            sum=sum+c[i];
        printf("%lld\n",sum);
        T--;
    }
    return 0;
}
