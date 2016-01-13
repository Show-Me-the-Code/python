#include <cstdio>
#include <cstring>
int main()
{
    int n,m;
    while(scanf("%d",&n)!=EOF)
    {
        int a[10000+5],b[10000+5],num,v=0;
        memset(a,0,sizeof(a));
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
        printf("%d",v);
        for(int i=0;i<v;i++)
        {
            printf(" %d",b[i]);
        }
        printf("\n");
    }
    return 0;
}
