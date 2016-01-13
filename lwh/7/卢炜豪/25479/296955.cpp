#include <cstdio>
#include <cmath>
#include <cstring>
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int n;
        scanf("%d",&n);
        long long int add=1;
        while(n)
        {
            int k;
            scanf("%d",&k);
            add=add*k;
            n--;
        }
        if(add>pow(10,8))
            printf("TLE\n");
        else
            printf("AC\n");
        T--;
    }
}
