#include <cstdio>
#define maxn 26
long long int num[maxn];
void moo(int n,int i);
int main()
{
    num[0]=0;
    num[1]=3;
    for(int i=2;i<maxn;i++)
    {
        num[i]=2*num[i-1]+2+i;
    //    printf("%lld\n",num[i]);
    }

    int N,i;
    while(scanf("%d",&N)!=EOF)
    {
        if(N<=3)
            moo(N,1);
        else
        {
            for(i=2;i<30;i++)
            {
                if(N>num[i-1]&&N<=num[i])
                break;
            }
            moo(N,i);
        }
    }
    return 0;
}
void moo(int n,int i)
{
    if(i==1)
    {
        if(n==1)
            printf("m\n");
        else
            printf("o\n");
    }
    while(i!=1)
    {
        if(n==num[i])
        {
            printf("o\n");
            break;
        }
        if(n<=num[i-1]+i+2)
        {
            if(n<=num[i-1])
            {
                moo(n,i-1);
                return;
            }
            if(n==num[i-1]+1)
               {
                    printf("m\n");
                    break;
               }
            else
                {
                    printf("o\n");
                    break;
                }
        }
        if(n>num[i-1]+i+2)
        {
            moo(n-num[i-1]-i-2,i-1);
            return;
        }
    }

}
