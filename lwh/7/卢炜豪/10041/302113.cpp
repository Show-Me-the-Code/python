#include <cstdio>
#include<cstring>
#include <algorithm>
using namespace std;
int a[1000000+2];
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        memset(a,0,sizeof(a));
        int N,k;
        scanf("%d %d",&N,&k);
        for(int i=1;i<=k;i++)
        {
            int m,n;
            scanf("%d %d",&m,&n);
            for(;m<=n;m++)
            {
                a[m]++;
     //           printf("a[%d]=%d\n",m,a[m]);
            }
        }
        sort(a,a+N+1);
     //   for(int i=1;i<=N;i++)
     //       printf("a[%d]=%d\n",i,a[i]);
   //     sort(a,a+N);
     //   for(int i=1;i<=N;i++)
         //   printf("%d\n",a[i]);
        printf("%d\n",a[N/2+1]);

    }
}
