#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;
int a[1000000+10];long long int b[1000000+10];
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        int n,k;
        scanf("%d %d",&n,&k);
        for(int i=1;i<=k;i++)
        {
            int m,n;
            scanf("%d %d",&m,&n);
            a[m]=a[m]+1;
            a[n+1]=a[n+1]-1;
        }
        for(int i=1;i<=n;i++)
        {
            a[i]=a[i-1]+a[i];
         //   b[i]=b[i]+b[i-1]+a[i];
        }
        sort(a,a+n+1);
   //     for(int i=1;i<=n;i++)
    //        printf("b[%d]=%d\n",i,a[i]);
        printf("%d\n",a[(n+1)/2]);
    }
}
