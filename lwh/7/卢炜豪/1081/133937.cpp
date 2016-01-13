#include<stdio.h>
#define maxn 100
int main()
{
    int n;
    while(scanf("%d",&n)==1&&(n!=0))
    {
        int a[maxn];int count=0;
        for(int i=0;i<n;i++)
        scanf("%d",&a[i]);

        int min=a[0];
        int d=a[0];

        for(int i=1;i<n;i++)
        if(a[i]<a[0]) min=i;
       // printf("%d\n",min);

        for(int i=0;i<n;i++)
        {
            if(a[i]==a[min])
                count++;
        }
        //printf("count=%d\n",count);
        for(int i=0;i<count;i++)
            printf("%d ",a[min]);
            printf("%d ",d);

        for(int i=1;i<n;i++)
        {
            if(a[i]!=a[min])
                if(i!=n-1)
                printf("%d ",a[i]);
            else if(i==n-1)
                printf("%d",a[i]);

        }
        printf("\n");
    }
    return 0;
}
