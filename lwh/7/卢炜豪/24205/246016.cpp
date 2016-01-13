#include<stdio.h>
#include<math.h>
int main()
{
    int n,m,p,y,z;
    while(scanf("%d %d",&n,&m)!=EOF)
    {
        p=n;
        for(int i=1;i<m;i++)
        {
            n=n%1000;
            n=n*p;
        }
       // printf("%d\n",n);
        y=(n/10)%10;
        printf("%d",y);
        printf("%d\n",n%10);

    }
}
