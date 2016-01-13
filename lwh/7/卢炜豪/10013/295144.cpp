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
        for(int i=1;i<=N;i++)
        {
            int k;
            scanf("%d",&k);
            a[k]++;
            if(max<a[k])
            {
                max=a[k];
                out=k;
            }
        }
        printf("%d\n",out);
    }
    return 0;
}
