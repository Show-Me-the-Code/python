#include <stdio.h>
#include <string.h>

#define maxn 100000+10

long long int a[maxn];
long long int b[maxn];
int main()
{
    int N,M,Q,x,y,z;
    while(scanf("%d",&N)!=EOF)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        if(N==0)
            break;
        scanf("%d %d",&M,&Q);

        for(int i=0;i<M;i++)
        {
            scanf("%d %d %d",&x,&y,&z);
            a[x]=a[x]+z;
            a[y+1]=a[y+1]-z;
        }

        for(int i=1;i<=N;i++)
        {
            a[i]=a[i]+a[i-1];
            b[i]=b[i-1]+a[i]+b[i];
         //   printf("%d\n",b[i]);
        }

       // printf("%d\n",b[1]);

        for(int i=0;i<Q;i++)
        {
            scanf("%d %d",&x,&y);
            long long int sum=b[y]-b[x-1];
            printf("%lld\n",sum);
        }
    }

    return 0;
}
