#include <cstdio>
#include <cstring>
#define max 300
#define maxn 1001
char a[1000+2][300];
void cal();
int main()
{
    int n,i;
    cal();
    while(scanf("%d",&n)!=EOF)
    {
        int l=strlen(a[n]);
        for(i=l-1;i>=0;i--)
            printf("%c",a[n][i]);
        printf("\n");
    }
}
void cal()
{
    int n,i,k;
    for(n=1;n<=1001;n++)
    {
        if(n==1)
            a[1][0]='1';
        else if(n==2)
            a[2][0]='1';
        else
        {
            for(i=0;a[n-1][i]!=0||a[n-2][i]!=0;i++)
            {
                if(a[n][i]!=0)
                    a[n][i]-='0';
                a[n][i]+=a[n-1][i]+a[n-2][i]-'0';
                if(a[n-1][i]==0||a[n-2][i]==0)
                    a[n][i]+='0';
                while(a[n][i]>'9')
                {
                    a[n][i]-=10;
                    a[n][i+1]+=1;
                }
                if(a[n][i+1]!=0)
                    a[n][i+1]+='0';
            }
        }
    }
}
