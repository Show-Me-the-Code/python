#include <cstdio>
int main()
{
    int n,del,a[100000+5],right[100000+5];
    scanf("%d %d",&n,&del);
    if(del<=0||del>n)
        printf("nothing to do");
    else
    {
        
    
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
        right[i]=i+1;
    }
    right[del-1]=del+1;
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
