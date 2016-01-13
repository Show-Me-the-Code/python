#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxn 500000+10
using namespace std;
int un[maxn];
int ans[2000];
int main()
{
    int n;
    un[1]=1;un[2]=2;un[3]=3;un[4]=5;
    int v=5,w=5;
   // memset(book,0,sizeof(book));
   // book[1]=1;book[2]=1;book[3]=1;book[5]=1;
    while(v<maxn)
    {
        int t=un[w-3];
        for(int i=2;i<=4;i++)
        {
            un[v]=t*un[i];
            v++;
            if(i==4) w++;
        }
    }
    sort(un,un+maxn);
    //for(int i=1;i<90010;i++)
      //  printf("%d\n",un[i]);
    int k=1;
    for(int i=1;i<maxn;)
    {
        int t=un[i];
        for(int j=i+1;;j++)
        {
            if(un[j]!=t)
            {
                ans[k]=t;
                k++;
                i=j;
                break;
            }
        }
    }
  //  for(int i=1;i<=1100;i++)
      //  printf("a[%d]=%d\n",i,ans[i]);
    while(scanf("%d",&n)!=EOF)
    {
        printf("%d\n",ans[n]);
    }
}
