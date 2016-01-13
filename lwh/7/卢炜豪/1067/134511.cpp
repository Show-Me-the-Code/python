#include<stdio.h>
int main()
{
    int g,m,x;
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int index=0;
        for(g=1;g<n;g++)
        {
            for(m=1;m<n-g;m++)
            {
                x=n-m-g;
                if(x%3!=0)
                    continue;
                int money;
                money=5*g+3*m+x/3;
                if(money==n)
                    index++;
            }
        }
        printf("%d\n",index);
    }
}
