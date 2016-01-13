#include<stdio.h>
int main()
{
    int n;int x;
    while(1)
    {
        scanf("%d",&n);
        if(n==0) break;
        int i;int a[n];int b[n];
        for(i=0;i<n;i++)
        {
           scanf("%d",&x);
           a[i]=x;
           b[i]=x;
         
        }

        int c;int q;
        for(q=0;q<n;q++)
        {
            if(a[q]<a[q+1]) a[q+1]=a[q];
            else if(a[q]>a[q+1]) a[q]=a[q+1];

        }
         int ha;
        ha=a[n-1];int w;
        for( w=0;w<n;w++)
        {
            if(b[w]==ha)

            break;
        }
      

        b[w]=b[0];
        b[0]=ha;
        for(int e=0;e<n;e++)
        {
            printf("%d ",b[e]);
        }
        printf("\n");

    }
}
