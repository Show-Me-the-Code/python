#include <cstdio>
#include <stack>
using namespace std;
int main()
{
    int carriage[1005],n;
    while(scanf("%d",&n)==1)
    {
        if(n==0)
            break;
        stack<int>station;
        while(scanf("%d",&carriage[1])!=0)
        {
            if(carriage[1]==0)
            {
                printf("\n");
                break;
            }
        for(int i=2;i<=n;i++)
            scanf("%d",&carriage[i]);
        int in=1,out=1;
        int suit=1;
        for(;out<=n;)
        {
            if(in==carriage[out])
            {
                in++;out++;
            }
            else if(station.empty()==0&&station.top()==carriage[out])
            {
                station.pop();
                out++;
            }
            else if(in<=n)
            {
                station.push(in++);
            }
            else
            {
                suit=0;
                break;
            }
        }
        if(suit==1)
            printf("Yes\n");
        else printf("No\n");

        }

    }
}
