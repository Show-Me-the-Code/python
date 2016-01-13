#include <cstdio>
#include <cstring>
#define maxn 300000
long long int sum[maxn]={0};
long long int book[maxn]={0};
const char *s[2]={"Stay here","I will go with you"};
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        memset(sum,0,T);
        memset(book,0,T);
        int N,m,flag=1;
        long long int input;
        scanf("%d %d",&N,&m);
        for(int i=1;i<=N;i++)
        {
            scanf("%lld",&input);
            sum[i]=(sum[i-1]+input%m)%m;
            book[sum[i]]++;
        }
        for(int i=1;i<=N;i++)
        {
            if(book[sum[i]]>1)
            {
                flag=0;
                break;
            }
            if(sum[i]==0&&book[sum[i]]>0)
            {
                flag=0;
                break;
            }
        }
        printf("%s\n",s[flag]);

    }
}
