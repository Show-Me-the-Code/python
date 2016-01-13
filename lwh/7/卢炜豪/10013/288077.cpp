#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

int main()
{
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        int book[100000+5],a[1000+5];
        memset(book,0,sizeof(book));
        int k;
        int max=-1;
        for(int i=0;i<N;i++)
        {
            scanf("%d",&a[i]);
            book[a[i]]++;
            if(book[a[i]]>max)
                max=book[a[i]];
        }
       // printf("!%d\n",book[5]);

    //    sort(book,book+N);


     //   printf("max=%d\n",max);

        for(int i=0;i<N;i++)
        {
      //      printf("a[%d]=%d book[%d]=%d\n",i,a[i],a[i],book[a[i]]);
            if(book[a[i]]==max)
            {
                printf("%d\n",a[i]);
                break;
            }
        }

    }
}
