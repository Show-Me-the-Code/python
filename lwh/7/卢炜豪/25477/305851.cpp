#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int main()
{
    int T;scanf("%d",&T);
    while(T--)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        if(a%b==0)
            printf("BMBMB\n");
        else
            printf("ANANA\n");
    }
}

/*void dfs(int n,int v,int qa)
{
    if(qa==v)
    {
       printf("%s\n",s);
        if(strcmp(s,t)>0)
        {
            ans++;
           // return ;
        //    printf("ans=%d\n",ans);
        }//   qa=0;

    }
    for(char j='0';j<='9';j++)
    {
        s[n]=j;
        printf("i=%d\n",i);
        dfs(a[i],v,qa+1);
    }

    return;
}*/
