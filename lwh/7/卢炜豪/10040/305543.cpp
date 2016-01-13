#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int a[12],i;
long long int ans=0;
char s[12],t[12];
void dfs(int n,int v,int qa);
int main()
{
    while(scanf("%s",s)!=EOF)
    {
        if(s[0]=='#') break;
        ans=0,i=0;
        scanf("%s",t);
        memset(a,0,sizeof(a));
        int len=strlen(s),QAnum=0,v=0;
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
            dfs(a[0],v,0);
            printf("%lld\n",ans);

    }
}

void dfs(int n,int v,int qa)
{
  //  printf("i=%d\n",i);
    if(qa>=v)
    {
     //   printf("%s\n",s);
        if(strcmp(s,t)>0)
        {
            ans++;
      //      printf("ans=%d\n",ans);
        }
        return;
    }
    for(char j='0';j<='9';j++)
    {
        s[n]=j;
        i++;
        dfs(a[i],v,qa+1);
        i=0;
    }

    return;
}
