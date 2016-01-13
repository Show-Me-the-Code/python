#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n==0)
            break;
        long long int a[10000+10],mid;
        for(int i=0;i<n;i++)
            scanf("%lld",&a[i]);
            sort(a,a+n);
        if(n%2==0)
            mid=a[n/2];
        else
            mid=a[n+1/2];
     //   printf("%lf\n",a[n-1]-(fabs(a[n-1]-a[0]))/2);
      // printf("mid=%lld\n",mid);
        long long int last=0;
        for(int i=0;i<n;i++)
        {
            last=last+fabs(a[i]-mid);
        }
        printf("%lld\n",last);

    }
    return 0;
}
