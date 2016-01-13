#include<stdio.h>
#include<math.h>
int main()
{
    int n,m,p,y,z;
    while(scanf("%d %d",&n,&m)!=EOF)
    {
        if(m!=0)
        {
        p=n;
        for(int i=1;i<m%20;i++)
        {
            n=n%1000;
            n=n*p;
        }
       // printf("n=%d\n",n);
       if(n>9)
       {
        y=(n/10)%10;
        printf("%d",y);
        printf("%d\n",n%10);
       }
       else if(n<10)
        printf("0%d\n",n);
        }

        else
            printf("01\n");

    }
}
