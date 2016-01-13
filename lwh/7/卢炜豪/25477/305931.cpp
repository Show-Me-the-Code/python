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
        if(a>=b)
            printf("BMBMB\n");
        else
            printf("ANANA\n");
    }
}
