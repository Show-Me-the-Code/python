#include <cstdio>
int main()
{
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        int a[100000+10],max=0,out;
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
