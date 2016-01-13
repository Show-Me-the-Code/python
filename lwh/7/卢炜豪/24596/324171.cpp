#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
struct Crane
{
    int x,y,r;
};
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int num;
        int ans = 0,area=0;
        scanf("%d",&num);
        struct Crane crane[20];

        for(int i=0; i<num; i++)
        {
            scanf("%d %d %d",&crane[i].x,&crane[i].y,&crane[i].r);
        }

        for(int i=0; i<num-1; i++)
        {
            for(int j=i; j<num-1; j++)
            {
                int dis = (crane[j].x-crane[j+1].x) * (crane[j].x-crane[j+1].x);
                if(dis > (crane[j].r + crane[j+1].r) * (crane[i].r + crane[j+1].r));
                    area += crane[j].r * crane[j].r;
            }
            if(area>ans)
                ans=area;
                area = 0;
        }
        printf("%d\n",ans);
    }
    return 0;
}
