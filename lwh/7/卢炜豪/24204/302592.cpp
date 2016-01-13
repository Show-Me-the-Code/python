#include <cstdio>
#include <cstring>
int main()
{
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        if(!N)
            return 0;
        int a[100000+5],b[100000+5];
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        int M,Q;scanf("%d %d",&M,&Q);
        for(int i=1;i<=M;i++)
        {
            int m,n,c;scanf("%d %d %d",&m,&n,&c);
            a[m]=c+a[m];
          //  b[m]=a[m];
            a[n+1]=-c+a[n+1];
          //  b[n+1]=a[n+1];
        }
       // for(int i=1;i<=N;i++) printf("before a[%d]=%d\n",i,a[i]);
       long long int sum=0;
       for(int i=1;i<=N;i++)
       {
           a[i]=a[i]+a[i-1];
           b[i]=b[i]+b[i-1]+a[i];
       }
       for(int i=1;i<=Q;i++)
       {
           int p,q;scanf("%d %d",&p,&q);
           sum=b[q]-b[p-1];
           printf("%lld\n",sum);
       }

    }
}
