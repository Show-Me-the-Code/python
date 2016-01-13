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
        double add=1;
        while(n)
        {
            double k;
            scanf("%lf",&k);
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
