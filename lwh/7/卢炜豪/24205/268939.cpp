#include <stdio.h>
#include <math.h>

int main()
{
    int n,m;
    while(scanf("%d %d",&n,&m)==2&&(n!=0&&m!=0))
    {
        int k=1;
        n=n%100;
        while(m>0)
        {
            if(m%2)
                k=(k*n)%100;
            m/=2;
            n=(n*n)%100;
        }
        if(k<10)
        printf("0%d\n",k);
        else
        printf("%d\n",k);

    }
}
