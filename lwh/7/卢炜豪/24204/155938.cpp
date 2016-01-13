#include<stdio.h>
#define maxn 100005
int add();
int serach();
int main()
{
    //freopen("dataflip.txt")
    int a[maxn],N,M,Q,ai,bi,ci,di,ei;
    while(scanf("%d",&N)==1)
    {
    int f=1;
    if(N==0) break;
    scanf("%d %d",&M,&Q);
    for(int i=1;i<=N;i++)
    {
        a[i]=f;
        f++;
    }
    for(int i=0;i<M;i++)
    {
        scanf("%d %d %d",&ai,&bi,&ci);
        for(int j=ai;j<=bi;j++)
        {
            a[j]=a[j]+ci;
        }
      //   for(int i=1;i<=N;i++) printf("a[%d]=%d\n",i,a[i]);
    }
   // for(int i=0;i<N;i++) printf("a[%d]=%d\n",a[i]);
    for(int i=0;i<Q;i++)
    {
        scanf("%d %d",&di,&ei);
        long long int sum=0;
        for(int j=di;j<=ei;j++)
        {
            sum=sum+a[j];
        }
        printf("%lld\n",sum);
    }

    }
}
