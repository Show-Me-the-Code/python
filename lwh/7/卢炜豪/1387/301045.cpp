#include <cstdio>
int main()
{
    int n,del,a[100000+5],right[100000+5];
    scanf("%d %d",&n,&del);
     for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            if(i!=n)
                right[i]=i+1;
            else
                right[i]=0;
        }
        right[0]=1;
    if(del<0||del>n)
        printf("nothing to do");
    else if(del==1)
        for(int i=2;i<=n;i++)
        {
            if(i!=n)
                printf("%d ",a[i]);
            else
                printf("%d",a[i]);
        }

    else
    {
        right[del-1]=del+1;
        right[del]=0;
        int t=1;
        for(int i=1;i<n;i++)
        {
            if(i!=n)
                printf("%d ",a[t]);
            else
                printf("%d",a[t]);

            t=right[t];
        }
    }
    return 0;

}
