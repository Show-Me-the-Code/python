#include <stdio.h>
int main()
{
    int n, m;
    while(scanf("%d %d",&n,&m)==2)
    {
        if(n==0&&m==0)
            return 0;
            if(n==1||m==1)
                printf("1\n");
            else
            {
                int sum=1;
                int temp=2;
                n--;m--;
                int index=n*m;
                while(index>0)
                {
                    if(index%2==1)
                        sum=sum*temp%10007;
                    index/=2;
                    temp=temp*temp%10007;
                }
                printf("%d\n",sum);
            }


    }
}
