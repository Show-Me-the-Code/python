#include <cstdio>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n%2||n<=2)
            printf("1\n");
        else if(n%2==0)
        {
            int count=0;
            while(1)
            {
                n/=2;
                 count++;
                 if(n==1)
                    break;
                 if(n%2&&n!=1)
                {
                    count++;
                    break;
                }
            }
            printf("%d\n",count);
        }
    }
}
