#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int a[1002];
        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
            scanf("%d",&a[i]);
        sort(a,a+N);
        for(int i=0;i<N;i++)
            printf("%d\n",a[i]);
    }
}
