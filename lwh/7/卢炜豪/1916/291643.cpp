#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
struct dp
{
   int start,end;
};
int main()
{
    int T,z=1;
    struct dp s[1005];
    scanf("%d",&T);
    while(z<=T)
    {
        int n,x,y;
        scanf("%d",&n);

        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&s[i].start,&s[i].end);
        }

        for(int i=1;i<n;i++)
        {
            for(int j=0;j<n-i;j++)
            {
                if(s[j].end>s[j+1].end)
                {
                    int temp=s[j].end;
                    s[j].end=s[j+1].end;
                    s[j+1].end=temp;
                }
            }
        }
        int sum=1;
        int start1=s[0].start,end1=s[0].end;
        for(int i=1;i<n;i++)
        {
            if(s[i].start>=end1)
            {
                end1=s[i].end;
                sum++;
            }
        }
        if(n==0)
        printf("Case %d: 0\n",z);
        else printf("Case %d: %d\n",z,sum);
        z++;

    }
}
