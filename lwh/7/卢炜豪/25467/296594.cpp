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
        int n;long long int a[10000+5];
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lld",&a[i]);
      //  sort(a,a+n);
        long long int sum1=0,sum2=0;
        for(int i=0;i<n;i++)
            sum1=sum1+a[i];
            sum1=sum1-a[0];
        for(int i=n-1;i>=0;i--)
            sum2=sum2+a[i];
            sum2=sum2-a[n-1];
            sum1=fabs(sum1);
            sum2=fabs(sum2);
          //  printf("%lld %lld\n",sum1,sum2);
        printf("%lld\n",max(sum1,sum2));
        T--;
    }
    return 0;
}
