#include<stdio.h>
#define maxn 1005
int main()
{
    int n,m;
    while(scanf("%d %d",&n,&m)==2&&(n!=0&&m!=0))
    {
        int a[maxn],b[maxn];
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        for(int i=0;i<n;i++)
        {
            int k;
            k=(i+m)%n;
            b[k]=a[i];
        }
        for(int i=0;i<n;i++)
        {
            if(i==n-1) printf("%d\n",b[i]);
                else printf("%d ",b[i]);
        }
    }
}
