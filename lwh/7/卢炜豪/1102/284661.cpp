#include<stdio.h>
#include<string.h>

#define maxn 10000

int book[maxn],a[maxn],n;
void dfs(int step);

int main()
{
    memset(book,0,sizeof(book));
    scanf("%d",&n);
    int sum=1;
    for(int i=n;i>0;i--)
        sum=sum*i;
    printf("%d\n",sum);
    dfs(1);

    return 0;

}

void dfs(int step)
{
    if(step==n+1)
    {
        for(int j=1;j<n;j++)
            printf("%d ",a[j]);
        printf("%d\n",a[n]);
    }

    for(int i=1;i<=n;i++)
    {
        if(book[i]==0)
        {
            a[step]=i;
            book[i]=1;

            dfs(step+1);
            book[i]=0;
        }
    }

    return;

}
