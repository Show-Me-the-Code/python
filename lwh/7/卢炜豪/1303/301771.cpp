#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int n,m;
    while(scanf("%d",&n)!=EOF)
    {
        int a[5000+2],b[5000+2],c[5000+2],v=0;
        for(int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        int m;
        scanf("%d",&m);
        for(int i=1;i<=m;i++)
            scanf("%d",&b[i]);
        int len=min(n,m);
        if(len==n)
        {
            for(int i=1;i<=len;i++)
            {
                for(int j=1;j<=m;j++)
                {
                    if(a[i]==b[j])
                    {
                        c[v]=a[i];
                        v++;
                        break;
                    }
                }
            }
        }
        else if(len==m)
        {
            for(int i=1;i<=len;i++)
            {
                for(int j=1;j<=n;j++)
                {
                    if(b[i]==a[j])
                    {
                        c[v]=b[i];
                        v++;
                        break;
                    }
                }
            }
        }
        printf("%d",v);
        for(int i=0;i<v;i++)
            printf(" %d",c[i]);
        printf("\n");
    }
    return 0;
}
