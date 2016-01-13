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
        else if(a%b==1)
            printf("ANANA\n");
    }
}
