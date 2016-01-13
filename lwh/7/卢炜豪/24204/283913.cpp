#include <stdio.h>
#include <string.h>

#define maxn 100000+2

int main()
{
    int N,ai[maxn],bi[maxn],ci[maxn];
    while(scanf("%d",&N)==1&&N!=0)
    {
        memset(ai,0,sizeof(ai));
        memset(bi,0,sizeof(bi));

        int n,a,b,c,m;
        scanf("%d %d",&m,&n);

        for(int j=0;j<m;j++)
        {
            scanf("%d %d %d",&a,&b,&c);
            bi[a]=bi[a]+c;
            bi[b+1]=bi[b+1]-c;

        }



        for(int i=1;i<=N;i++)
        {
          ai[i]=ai[i-1]+bi[i];
        }

         for(int j=0;j<n;j++)
        {
            int sum=0;
            scanf("%d %d",&a,&b);
            for(int i=a;i<=b;i++)
                sum=sum+ai[i];
            printf("%d\n",sum);
        }

    }
}
