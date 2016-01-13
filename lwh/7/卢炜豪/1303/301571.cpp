#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxn 100000000
using namespace std;
int a[maxn],b[maxn];
int main()
{
    int n,m;
    while(scanf("%d",&n)!=EOF)
    {
        int num,v=0;
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&num);
            a[num]=1;
        }
        scanf("%d",&m);
        for(int i=1;i<=m;i++)
        {
            scanf("%d",&num);
            if(a[num]==1)
            {
                b[v]=num;
                v++;
            }
        }
       // printf("v=%d\n",v);
        sort(b,b+v);
        if(v==0)
            printf("0\n");
       // printf(" %d",b[0]);
       else if(v!=0)
       {
           printf("%d",v);

        for(int i=0;i<v;i++)
        {
            printf(" %d",b[i]);
        }
        printf("\n");
       }
    }
    return 0;
}
