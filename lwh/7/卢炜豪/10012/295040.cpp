#include <stdio.h>
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        int m,n,b;
        scanf("%d %d %d",&m,&n,&b);
        if(m%b==0||n%b==0)
            printf("yes\n");
        else printf("no\n");
    }
}
