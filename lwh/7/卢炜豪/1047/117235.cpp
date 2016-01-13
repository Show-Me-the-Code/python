#include<stdio.h>
int main()
{
    int n,x;
    while(1)
    {
        scanf("%d %d",&n,&x);if(n==0&&x==0) break;
        int a[n+1],b[n+1];
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            b[i]=a[i];
        }

    //   for(int i=0;i<n+1;i++) printf("a[%d]=%d ",i,a[i]);
        int t;
        for(t=0;t<n;t++)
        {
            int b=0;
            if(x<=a[t])
            {

                a[t]=x;
                b=1;
            }
            if(b==1) break;


        }
      printf("t=%d n=%d x=%d\n",t,n,x);
        if(a[t]==a[n])
        {
            for(int i=0;i<n;i++)
            {
                printf("%d ",a[i]);
            }
            printf("%d ",x);
            printf("\n");
        }
        else if(a[t]!=a[n])
        {
            for(int i=0;i<=t;i++)
                printf("%d ",a[i]);
            for(int w=t;w<n;w++)
            {

                printf("%d ",b[w]);
            }
            printf("t=%d",t);
            printf("\n");
        }


    }
}
