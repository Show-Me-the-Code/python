#include <stdio.h>
#include <math.h>

int main()
{
    int T;scanf("%d",&T);
    while(T--)
    {
        long long int n;
        scanf("%lld",&n);
        long long int k=1;
        long long int m=n;
        n=n%100;
        while(m>0)
        {
            if(m%2)
                k=(k*n)%10;
            m/=2;
            n=(n*n)%10;
        }
        printf("%lld\n",k);

    }
}
