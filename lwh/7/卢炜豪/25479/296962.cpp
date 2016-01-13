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
         int a[6];
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        for(int i=0;i<n;i++)
            add=add*a[i];
        if(add>pow(10,8))
            printf("TLE\n");
        else
            printf("AC\n");
        T--;
    }
}
