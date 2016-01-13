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
        int n,c[10000+5];
        c[0]=0;int max=-1;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&c[i]);
        sort(c,c+n);
        int sum=0;
        for(int i=1;i<n;i++)
            sum=sum+c[i];
        printf("%d\n",sum);
        T--;
    }
    return 0;
}
