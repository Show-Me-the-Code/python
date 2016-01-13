#include <stdio.h>
int main()
{
    int n, x, end=0;
    while(scanf("%d %d",&n,&x)&&n&&x)
    {

    for (int i = 2; i <= n; i++)
    {
        end= (end + x) % i;
    }
    printf ("%d\n", end+1);

    }
}
