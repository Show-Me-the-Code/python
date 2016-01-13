#include<stdio.h>
int main()
{
    int n;int x;
    while(scanf("%d",&n)!=EOF)
    {
        int a[n];int add=1;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&x);
            a[i]=x;

        }
        for(int i=0;i<n;i++)
        {
            if(a[i]%2!=0)
            add=a[i]*add;

        }
        printf("%d\n",add);
    }
}
