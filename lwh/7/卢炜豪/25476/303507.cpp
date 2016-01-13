#include <cstdio>
#include <cstring>
#define maxn 300000
int  sum[maxn]={0};
int  book[maxn]={0};
const char *s[2]={"Stay here","I will go with you"};
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        memset(sum,0,sizeof(sum));
        memset(book,0,sizeof(book));
        int N,m,flag=1;
        int input;
        scanf("%d %d",&N,&m);
        for(int i=1;i<=N;i++)
        {
            scanf("%d",&input);
            sum[i]=(sum[i-1]+input%m)%m;
            book[sum[i]]++;
            /*
        对o(n^2)的公式 转化出另外的公式，
        (sum[j]-sum[i])%m==0=> sum[j]%m ==sum[i]%m，
        然后用表保存出现的余数进行优化*/
        //book数组是进行转化的关键。如果出现sum[j]%m ==sum[i]%m，即有多组成立，累加上去即可
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
