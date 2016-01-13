#include <cstdio>
#include <cstring>
int a[100000+10];
int main()
{
    memset(a,0,sizeof(a));
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        int max=0,out;
        memset(a,0,sizeof(a));
        for(int i=1;i<=N;i++)
        {
            int k;
            scanf("%d",&k);
            a[k]++;
           // printf("max=%d a[%d]=%d\n",max,k,a[k]);
            if(max<a[k])
            {
                max=a[k];

            }
        }
        for(int i=1;i<=N;i++)
            if(a[i]==max)
        {
            printf("%d\n",i);
            break;
        }
    }
    return 0;
}
