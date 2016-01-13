#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);

    while(T--)
    {
        int n,m,l,ans=0;
        int A[10000+5],B[10000+5],book[10000+5];
        memset(book,0,sizeof(book[0]));
        for(int i=0;i<10005;i++)
            A[i]=-1;
        scanf("%d %d %d",&n,&m,&l);
        //ans = n;

        for(int i=1;i<=m;i++)
        {
            int x,y;
            scanf("%d %d",&x,&y);
            A[x]=y;
        }
        for(int i=1; i<=l; i++)
        {
            scanf("%d",&B[i]);
            //book[B[i]]=1;
        }
        //sort(B,B+l);
        for(int i=1; i<=l; i++)
        {
            int j=B[i];
            while(A[j]!=-1)
            {
                if(book[A[j]]==1)
                    break;
                book[A[j]]=1;
                book[j]=1;
                j=A[j];
              //  printf("j=%d\n",j);
            }

        }
        for(int i=1; i<=n; i++)
        {
            //printf("book[%d]=%d\n",i,book[i]);
            if(book[i]==1)
                ans++;
        }
        printf("%d\n",ans);
    }
}
