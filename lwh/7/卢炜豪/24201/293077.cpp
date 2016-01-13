#include <cstdio>
#include <algorithm>
#define maxn 100000+3
using namespace std;


int main()
{
    pair<int,int>mm[100000+3];
    int N,start[maxn],end[maxn];
    while(scanf("%d",&N)&&N)
    {
        for(int i=0;i<N;i++)
        {
           scanf("%d %d",&start[i],&end[i]);
        }
        for(int i=0;i<N;i++)
        {
            mm[i].first=end[i];
            mm[i].second=start[i];
        }
        sort(mm,mm+N);
     //   printf("\n");
       // for(int i=0;i<N;i++)
       //    printf("%d %d\n",mm[i].first,mm[i].second);
        int sum=0,end1=0;
        for(int i=0;i<N;i++)
        {
            if(mm[i].second>=end1)
            {
                sum++;
                end1=mm[i].first;
            //    printf("i=%d sum=%d end1=%d\n",i,sum,end1);
            }
        }
        printf("%d\n",sum);

    }
}
