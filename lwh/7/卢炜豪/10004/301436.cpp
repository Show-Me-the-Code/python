#include <stdio.h>
int main()
{
    int n, x;
    while(scanf("%d %d",&n,&x)==2)
    {
        int end=0;
        if(n==0&&x==0)
            return 0;

    for (int i = 2; i <=n; i++)
    {
        end= (end + x) % i;
    }
    printf ("%d\n", end+1);


    }
}
