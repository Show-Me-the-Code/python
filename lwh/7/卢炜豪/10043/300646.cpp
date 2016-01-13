#include <cstdio>
#include <cstring>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        char b[21],g[21],c[10];
        scanf("%s %s %s",b,g,c);
        printf("%s will survive\n",g);
    }
    return 0;
}
