#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int a[20],i,v;
long long int ans=0;
char s[20],t[20];
void dfs(int n);
int main()
{
    while(scanf("%s",s)!=EOF)
    {
        if(s[0]=='#') break;
        ans=0,i=0,v=0;
        scanf("%s",t);
        memset(a,0,sizeof(a));
        int len=strlen(s),QAnum=0;
        for(int i=0;i<len;i++)
            if(s[i]=='?')
            {
                QAnum++;//统计问号的个数
                a[v]=i;//问号的下标
           //     printf("a[%d]=%d\n",v,a[v]);
                v++;
            }
         //   printf("%d\n",v);
      //   for(int i=a[0];i<=a[v-1];i++)
            dfs(0); //问号数组的下标 当前问号的编号
            printf("%lld\n",ans);

    }
}

void dfs(int n)
{
  //  printf("n=%d\n",n);
    if(n==v)
    {
      //  printf("%s\n",s);
        if(strcmp(s,t)>0)
            ans++;
        return;
    }
    for(char j='0';j<='9';j++)
    {
        s[a[n]]=j;
        dfs(n+1);
    }
    return;
}
