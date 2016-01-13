#include <stdio.h>
int main()
{
    int n, x, end=0;
    while(scanf("%d %d",&n,&x))
    {
        if(n==0&&x==0)
            return 0;
            if(n==1)
                printf("1\n");
    else
    {


    for (int i = 2; i <=n; i++)
    {
        end= (end + x) % i;
    }
    printf ("%d\n", end+1);
    }

    }
}
