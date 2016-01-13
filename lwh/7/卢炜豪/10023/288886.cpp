#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int i;
        long long int a[50];
        memset(a,0,sizeof(a));
        a[0]=0;a[1]=1;a[2]=1;
        if(n==1||n==2)
            printf("1\n");
        else if(n==0)
            printf("0\n");
        else if(n>2)
        {
            for(i=3;i<=n;i++)
            {
                if(a[i]==0)
                {
                a[i]=a[i-1]+a[i-2];
                }

            }

                printf("%lld\n",a[n]);
        }
    }
}
