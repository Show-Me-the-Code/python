#include <stdio.h>

#define maxn 100000+5

int a[maxn],b[maxn];
int main()
{
    int N,M,Q,x,y,z;
    while(scanf("%d",&N)!=EOF)
    {
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
            b[i]=b[i-1]+a[i];
         //   printf("%d\n",b[i]);
        }

        for(int i=0;i<Q;i++)
        {
            scanf("%d %d",&x,&y);
            printf("%d\n",b[y]-b[x-1]);
        }
    }

    return 0;
}
