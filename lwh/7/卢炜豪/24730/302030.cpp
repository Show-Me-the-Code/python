#include <cstdio>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n%2)
            printf("1\n");
        else if(n%2==0)
        {
            int count=0;
            while(n>3)
            {
                n/=2;
                 count++;
                if(n%2)
                    break;
            }
            printf("%d\n",count+1);
        }
    }
}
